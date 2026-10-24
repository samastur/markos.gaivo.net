#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render a single blog post the way Pelican would, without building the site.

The post is read, processed by the enabled plugins and rendered with the
theme's template by Pelican itself; only the generation of all other pages is
skipped. Posts it links to with {filename} or {static} are read on demand, so
those links resolve as on the real site.

Examples:
    preview_post.py articles/content/resurrection.md -o /tmp/preview.html
    cat draft.md | preview_post.py --name my-draft.md > preview.html
    preview_post.py post.md --setting SITEURL='"http://localhost:8000"'
"""

from os.path import (abspath, basename, dirname, exists, isfile, join, normpath,
                     relpath)
import argparse
import json
import os
import shutil
import sys
import tempfile

THIS_DIR = abspath(dirname(__file__))
ARTICLES_DIR = join(THIS_DIR, 'articles')
REEXEC_GUARD = 'PREVIEW_POST_REEXECED'


def parse_args():
    parser = argparse.ArgumentParser(
        description='Render a preview of a single post with Pelican.')
    parser.add_argument(
        'input', nargs='?', default='-',
        help='post to render; "-" or nothing reads it from stdin')
    parser.add_argument(
        '-o', '--output', default='-',
        help='file to write the rendered page to; "-" is stdout '
             '(default: %(default)s)')
    parser.add_argument(
        '--name',
        help='path of the post relative to the content directory, used for '
             'resolving relative links, path metadata and choosing the '
             'reader (default: the input\'s own path if it is inside the '
             'content directory, else its file name, or "preview.md" for '
             'stdin)')
    parser.add_argument(
        '--page', action='store_true',
        help='render the post as a page instead of an article')
    parser.add_argument(
        '--project', default=ARTICLES_DIR,
        help='Pelican project directory whose virtual env is used '
             '(default: %(default)s)')
    parser.add_argument(
        '--settings',
        help='Pelican settings file (default: PROJECT/pelicanconf.py)')
    parser.add_argument(
        '--content',
        help='content directory (default: PATH from the settings)')
    parser.add_argument(
        '--setting', action='append', default=[], metavar='KEY=VALUE',
        help='override a Pelican setting; VALUE is parsed as JSON if '
             'possible, otherwise used as a string; can be repeated')
    parser.add_argument(
        '--python',
        help='Python interpreter with Pelican installed (default: '
             'PROJECT/.venv/bin/python, falling back to `uv run`)')
    parser.add_argument(
        '-q', '--quiet', action='store_true',
        help='only report errors, not Pelican warnings')
    return parser.parse_args()


def ensure_pelican(args):
    """Re-exec this script in the virtual env that has Pelican installed."""
    try:
        import pelican  # noqa: F401
        return
    except ImportError:
        pass

    if os.environ.get(REEXEC_GUARD):
        sys.exit('preview_post.py: Pelican is not installed in {0}'.format(
            sys.executable))
    os.environ[REEXEC_GUARD] = '1'

    script = abspath(__file__)
    python = args.python or join(abspath(args.project), '.venv', 'bin',
                                 'python')
    if exists(python):
        os.execv(python, [python, script] + sys.argv[1:])
    os.execvp('uv', ['uv', 'run', '--quiet', '--project', args.project,
                     'python', script] + sys.argv[1:])


def parse_overrides(pairs):
    overrides = {}
    for pair in pairs:
        key, sep, value = pair.partition('=')
        if not sep or not key:
            sys.exit('preview_post.py: --setting expects KEY=VALUE, got '
                     '{0!r}'.format(pair))
        try:
            overrides[key] = json.loads(value)
        except ValueError:
            overrides[key] = value
    return overrides


def load_settings(args, output_dir):
    from pelican.settings import read_settings

    settings_file = abspath(args.settings or join(args.project,
                                                  'pelicanconf.py'))
    # Settings like publishconf.py import their siblings by module name.
    sys.path.insert(0, dirname(settings_file))
    overrides = parse_overrides(args.setting)
    if args.content:
        overrides['PATH'] = abspath(args.content)
    # Never touch the real output directory or content caches.
    overrides.update({
        'OUTPUT_PATH': output_dir,
        'DELETE_OUTPUT_DIRECTORY': False,
        'CACHE_CONTENT': False,
        'LOAD_CONTENT_CACHE': False,
    })
    return read_settings(settings_file, override=overrides)


class LazyContent(dict):
    """Source path -> content map that reads linked files on first use.

    Pelican resolves {filename} and {static} links by looking the target up
    in the context; instead of reading the whole site up front, only the
    files a preview actually links to are read.
    """

    def __init__(self, load):
        super().__init__()
        self._load = load

    def get(self, key, default=None):
        if key not in self:
            self[key] = self._load(key)
        value = super().get(key)
        return default if value is None else value


def make_loaders(settings, readers, context):
    from pelican.contents import Article, Page, Static
    from pelican.utils import posixize_path

    content_dir = settings['PATH']
    page_paths = [posixize_path(path) for path in settings['PAGE_PATHS']]

    def source(key):
        path = normpath(join(content_dir, key))
        if relpath(path, content_dir).startswith('..') or not isfile(path):
            return None
        return path

    def load_generated(key):
        if source(key) is None:
            return None
        is_page = any(key == path or key.startswith(path.rstrip('/') + '/')
                      for path in page_paths)
        try:
            return readers.read_file(
                base_path=content_dir, path=key,
                content_class=Page if is_page else Article,
                context=context)
        except Exception:
            return None

    def load_static(key):
        if source(key) is None:
            return None
        try:
            return readers.read_file(base_path=content_dir, path=key,
                                     content_class=Static, fmt='static',
                                     context=context)
        except Exception:
            return None

    return load_generated, load_static


def read_from(reader, cachers, virtual_paths, real_path):
    """Make Pelican use real_path whenever it asks for a virtual path."""
    def redirect(func):
        return lambda path: func(real_path if path in virtual_paths else path)

    reader.read = redirect(reader.read)
    # Readers and generators stamp files they read, even with caching off.
    for cacher in cachers:
        cacher._get_file_stamp = redirect(cacher._get_file_stamp)


def render(args, input_path, output_dir):
    from pelican import Pelican, signals
    from pelican.generators import ArticlesGenerator, PagesGenerator
    from pelican.log import init as init_logging
    from pelican.utils import file_suffix
    from pelican.writers import Writer
    import logging

    # Pelican logs to stdout by default, which would mix with the page.
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    init_logging(level=logging.ERROR if args.quiet else logging.WARNING,
                 handler=handler)

    settings = load_settings(args, output_dir)
    content_dir = settings['PATH']

    if args.name:
        name = args.name
    elif not relpath(input_path, content_dir).startswith('..'):
        name = relpath(input_path, content_dir)
    else:
        name = basename(input_path)
    virtual_path = abspath(join(content_dir, name))

    # Loads and registers the plugins exactly like a normal build.
    pelican = Pelican(settings)

    context = settings.copy()
    context['static_links'] = set()
    context['localsiteurl'] = settings['SITEURL']

    base = PagesGenerator if args.page else ArticlesGenerator

    class PreviewGenerator(base):
        def get_files(self, paths, exclude=None, extensions=None):
            return [relpath(virtual_path, content_dir)]

    generator = PreviewGenerator(
        context=context, settings=settings, path=content_dir,
        theme=pelican.theme, output_path=output_dir)
    load_generated, load_static = make_loaders(settings, generator.readers,
                                               context)
    context['generated_content'] = LazyContent(load_generated)
    context['static_content'] = LazyContent(load_static)

    fmt = file_suffix(virtual_path)
    if fmt not in generator.readers.readers:
        sys.exit('preview_post.py: no Pelican reader for "{0}" files; use '
                 '--name to give the post a known extension'.format(fmt))
    if input_path != virtual_path:
        # The generator refers to the post relative to the content directory.
        read_from(generator.readers.readers[fmt],
                  (generator, generator.readers),
                  {virtual_path, relpath(virtual_path, content_dir)}, input_path)

    generator.generate_context()
    signals.all_generators_finalized.send([generator])
    generator.refresh_metadata_intersite_links()

    if args.page:
        posts = (generator.pages + generator.hidden_pages +
                 generator.draft_pages)
    else:
        posts = (generator.articles + generator.hidden_articles +
                 generator.drafts)
    if not posts:
        sys.exit('preview_post.py: Pelican did not produce a post from the '
                 'input (see warnings above)')
    post = posts[0]

    # Same template arguments as the generators' generate_output().
    if args.page:
        signals.page_generator_write_page.send(generator, content=post)
        kwargs = {'page': post}
    else:
        signals.article_generator_write_article.send(generator, content=post)
        kwargs = {'article': post, 'category': getattr(post, 'category', None),
                  'blog': True}
        if post.status == 'draft':
            kwargs['all_articles'] = generator.articles

    writer = Writer(output_dir, settings=settings)
    writer.write_file(
        post.save_as, generator.get_template(post.template), generator.context,
        relative_urls=settings['RELATIVE_URLS'],
        override_output=hasattr(post, 'override_save_as'), url=post.url,
        **kwargs)
    return join(output_dir, post.save_as)


def main():
    args = parse_args()
    parse_overrides(args.setting)  # fail early, before waiting on stdin
    ensure_pelican(args)

    with tempfile.TemporaryDirectory(prefix='preview_post-') as tmp:
        output_dir = join(tmp, 'output')
        os.mkdir(output_dir)
        if args.input == '-':
            if sys.stdin.isatty():
                print('Reading the post from stdin (end with Ctrl-D)...',
                      file=sys.stderr)
            args.name = args.name or 'preview.md'
            input_path = join(tmp, 'input', basename(args.name))
            os.mkdir(dirname(input_path))
            with open(input_path, 'w', encoding='utf-8') as f:
                f.write(sys.stdin.read())
        else:
            input_path = abspath(args.input)
            if not isfile(input_path):
                sys.exit('preview_post.py: no such file: {0}'.format(
                    args.input))

        rendered = render(args, input_path, output_dir)

        if args.output == '-':
            with open(rendered, encoding='utf-8') as f:
                sys.stdout.write(f.read())
        else:
            shutil.copyfile(rendered, args.output)


if __name__ == '__main__':
    main()
