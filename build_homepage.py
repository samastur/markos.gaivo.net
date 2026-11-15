#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the pages in root/ that are not part of the blog.

root/index.html comes from homepage/about.md and homepage/template.html: the
Markdown becomes the content of <article class="about">, a leading "# Heading"
is wrapped in <header> like the hand-written page had. root/404.html and
root/500.html come from homepage/404.html and homepage/500.html.

The templates are Jinja, rendered like Pelican renders the blog: with the
blog's settings (articles/pelicanconf.py) and the theme's templates, so they
share its <head> (inlined stylesheet, theme toggle) and footer.

Examples:
    build_homepage.py            # write root/index.html, 404.html, 500.html
    build_homepage.py --edit     # open about.md in Aaron first, then build
    build_homepage.py -o -       # print the homepage instead of writing it
"""

from os.path import abspath, dirname, expanduser, join
import argparse
import os
import re
import shutil
import subprocess
import sys

THIS_DIR = abspath(dirname(__file__))
ARTICLES_DIR = join(THIS_DIR, 'articles')
HOMEPAGE_DIR = join(THIS_DIR, 'homepage')
SOURCE = join(HOMEPAGE_DIR, 'about.md')
TEMPLATE = 'template.html'
ROOT_DIR = join(THIS_DIR, 'root')
OUTPUT = join(ROOT_DIR, 'index.html')
# Other pages built from homepage/: template name -> file in root/
ERROR_PAGES = {'404.html': '404.html', '500.html': '500.html'}
# Where the blog is, as seen from the page (the theme's SITEURL). The error
# pages are served at whatever path was requested, so theirs is absolute.
HOMEPAGE_SITEURL = 'articles'
ERROR_PAGE_SITEURL = '/articles'

EDITOR = shutil.which('aaron') or expanduser('~/.local/bin/aaron')
EDITOR_PROFILE = 'Blog'

try:
    import jinja2
    import markdown
    from pelican.settings import read_settings
except ImportError:
    # Not running inside the articles uv env, so re-exec through it.
    os.execvp('uv', ['uv', 'run', '--project', ARTICLES_DIR,
                     'python', abspath(__file__)] + sys.argv[1:])


def render_content(text):
    html = markdown.markdown(text, extensions=['extra'], output_format='html')
    # Put the page title into <header>, as the article markup expects.
    html = re.sub(r'\A\s*(<h1>.*?</h1>)',
                  r'<header>\n\1\n</header>', html, flags=re.S)
    return html


def environment():
    """A Jinja environment like Pelican's, finding homepage/ and the theme."""
    settings = read_settings(join(ARTICLES_DIR, 'pelicanconf.py'))
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            [HOMEPAGE_DIR, join(settings['THEME'], 'templates')]),
        **settings['JINJA_ENVIRONMENT'])
    env.filters.update(settings['JINJA_FILTERS'])
    env.globals['CURRENT_YEAR'] = settings['CURRENT_YEAR']
    env.globals['THEME_STATIC_DIR'] = settings['THEME_STATIC_DIR']
    return env


def build(source=SOURCE, template=TEMPLATE, env=None):
    with open(source, encoding='utf-8') as f:
        content = render_content(f.read())
    env = env or environment()
    return env.get_template(template).render(content=content,
                                             SITEURL=HOMEPAGE_SITEURL)


def build_error_pages(env=None):
    env = env or environment()
    for template, name in ERROR_PAGES.items():
        path = join(ROOT_DIR, name)
        write(env.get_template(template).render(SITEURL=ERROR_PAGE_SITEURL),
              path)


def write(page, path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(page)
    print(path, file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description='Build the homepage from Markdown.')
    parser.add_argument('-o', '--output', default=OUTPUT,
                        help='where to write the homepage; "-" is stdout '
                             '(default: root/index.html). The error pages '
                             'are only written with the default.')
    parser.add_argument('--edit', action='store_true',
                        help='open about.md in Aaron before building')
    args = parser.parse_args()

    if args.edit:
        subprocess.run([EDITOR, '--profile', EDITOR_PROFILE, SOURCE],
                       stdout=subprocess.DEVNULL, check=True)

    env = environment()
    page = build(env=env)
    if args.output == '-':
        sys.stdout.write(page)
    else:
        write(page, args.output)
        if args.output == OUTPUT:
            build_error_pages(env)


if __name__ == '__main__':
    main()
