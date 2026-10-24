#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""List all tags used in the blog's posts, with how often each is used.

Tags are parsed with Pelican's own readers and metadata processors, so they
are split, cleaned up and grouped (by slug) exactly as on the generated site.

Examples:
    list_tags.py                      # text table, most used first
    list_tags.py --json               # JSON for other tools
    list_tags.py --status published   # only tags visible on the site
"""

from collections import Counter, defaultdict
from fnmatch import fnmatch
from os.path import abspath, dirname, exists, join, relpath
import argparse
import json
import os
import sys

THIS_DIR = abspath(dirname(__file__))
ARTICLES_DIR = join(THIS_DIR, 'articles')
REEXEC_GUARD = 'LIST_TAGS_REEXECED'


def parse_args():
    parser = argparse.ArgumentParser(
        description='List tags used in blog posts together with their '
                    'frequency.')
    parser.add_argument(
        '--project', default=ARTICLES_DIR,
        help='Pelican project directory whose virtual env is used '
             '(default: %(default)s)')
    parser.add_argument(
        '--settings',
        help='Pelican settings file (default: PROJECT/pelicanconf.py)')
    parser.add_argument(
        '--content',
        help='content directory to scan (default: PATH from the settings)')
    parser.add_argument(
        '--python',
        help='Python interpreter with Pelican installed (default: '
             'PROJECT/.venv/bin/python, falling back to `uv run`)')
    parser.add_argument(
        '--status', action='append',
        help='only count posts with this status; can be repeated '
             '(default: all except "skip")')
    parser.add_argument(
        '--sort', choices=('count', 'name'), default='count',
        help='sort order (default: %(default)s)')
    parser.add_argument(
        '--json', action='store_true', help='output JSON')
    parser.add_argument(
        '--full', action='store_true',
        help='parse whole posts with Pelican instead of only their '
             'metadata headers (slower, same result)')
    return parser.parse_args()


def ensure_pelican(args):
    """Re-exec this script in the virtual env that has Pelican installed."""
    try:
        import pelican  # noqa: F401
        return
    except ImportError:
        pass

    if os.environ.get(REEXEC_GUARD):
        sys.exit('list_tags.py: Pelican is not installed in {0}'.format(
            sys.executable))
    os.environ[REEXEC_GUARD] = '1'

    script = abspath(__file__)
    python = args.python or join(abspath(args.project), '.venv', 'bin',
                                 'python')
    if exists(python):
        os.execv(python, [python, script] + sys.argv[1:])
    os.execvp('uv', ['uv', 'run', '--quiet', '--project', args.project,
                     'python', script] + sys.argv[1:])


def find_sources(content_dir, settings, extensions):
    """Yield article source paths, relative to content_dir."""
    article_paths = settings['ARTICLE_PATHS'] or ['']
    excludes = set(settings['ARTICLE_EXCLUDES'])
    ignored = settings['IGNORE_FILES']

    for article_path in article_paths:
        top = join(content_dir, article_path)
        for root, dirs, files in os.walk(top, followlinks=True):
            dirs[:] = sorted(
                d for d in dirs
                if relpath(join(root, d), content_dir) not in excludes
                and not any(fnmatch(d, pattern) for pattern in ignored))
            for name in sorted(files):
                if any(fnmatch(name, pattern) for pattern in ignored):
                    continue
                if name.rsplit('.', 1)[-1].lower() in extensions:
                    yield relpath(join(root, name), content_dir)


def read_header(path):
    """Return the Markdown metadata block at the top of a file."""
    lines = []
    with open(path, encoding='utf-8-sig') as f:
        for number, line in enumerate(f):
            stripped = line.strip()
            if number == 0 and stripped == '---':
                lines.append(line)
                continue
            if not stripped or (lines and lines[0].strip() == '---'
                                and stripped in ('---', '...')):
                break
            lines.append(line)
    return ''.join(lines)


def read_metadata_fast(reader, path):
    """Parse only the tags and status of a Markdown file, the Pelican way."""
    from markdown import Markdown

    reader._source_path = path
    reader._md = Markdown(**reader.settings['MARKDOWN'])
    reader._md.convert(read_header(path))
    meta = {name: value for name, value in getattr(reader._md, 'Meta',
                                                     {}).items()
            if name.lower() in ('tags', 'status')}
    return reader._parse_metadata(meta)


def collect_tags(content_dir, settings, statuses=None, full=False):
    from pelican.readers import MarkdownReader, Readers

    readers = Readers(settings)
    default_status = settings['DEFAULT_METADATA'].get('status', 'published')
    counts = Counter()
    spellings = defaultdict(Counter)
    posts = 0

    for source in find_sources(content_dir, settings, readers.extensions):
        path = join(content_dir, source)
        reader = readers.readers[source.rsplit('.', 1)[-1].lower()]
        if not full and isinstance(reader, MarkdownReader):
            metadata = read_metadata_fast(reader, path)
        else:
            metadata = readers.read_file(content_dir, source).metadata

        status = str(metadata.get('status') or default_status).lower()
        if status == 'skip' or (statuses and status not in statuses):
            continue
        posts += 1
        for tag in set(metadata.get('tags') or []):
            counts[tag.slug] += 1
        for tag in metadata.get('tags') or []:
            spellings[tag.slug][tag.name] += 1

    tags = []
    for slug, count in counts.items():
        names = [name for name, _ in spellings[slug].most_common()]
        tags.append({'name': names[0], 'slug': slug, 'count': count,
                     'variants': names[1:]})
    return posts, tags


def main():
    args = parse_args()
    ensure_pelican(args)

    from pelican.settings import read_settings

    settings_file = abspath(args.settings or join(args.project,
                                                  'pelicanconf.py'))
    # Settings like publishconf.py import their siblings by module name.
    sys.path.insert(0, dirname(settings_file))
    settings = read_settings(settings_file)
    content_dir = abspath(args.content or settings['PATH'])
    statuses = {status.lower() for status in args.status or []}

    posts, tags = collect_tags(content_dir, settings, statuses, args.full)
    if args.sort == 'count':
        tags.sort(key=lambda tag: (-tag['count'], tag['name'].lower()))
    else:
        tags.sort(key=lambda tag: tag['name'].lower())

    if args.json:
        json.dump({'content': content_dir, 'posts': posts, 'tags': tags},
                  sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write('\n')
        return

    width = len(str(max([tag['count'] for tag in tags] or [0])))
    for tag in tags:
        line = '{0:>{1}}  {2}'.format(tag['count'], width, tag['name'])
        if tag['variants']:
            line += '  (also: {0})'.format(', '.join(tag['variants']))
        print(line)
    print('\n{0} tags in {1} posts'.format(len(tags), posts), file=sys.stderr)


if __name__ == '__main__':
    main()
