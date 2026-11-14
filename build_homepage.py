#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build root/index.html from homepage/about.md and homepage/template.html.

The Markdown becomes the content of <article class="about">; a leading
"# Heading" is wrapped in <header> like the hand-written page had. The
template's {{ year }} is replaced with the current year.

Examples:
    build_homepage.py            # write root/index.html
    build_homepage.py --edit     # open about.md in Aaron first, then build
    build_homepage.py -o -       # print the page instead of writing it
"""

from datetime import date
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
TEMPLATE = join(HOMEPAGE_DIR, 'template.html')
OUTPUT = join(THIS_DIR, 'root', 'index.html')

EDITOR = shutil.which('aaron') or expanduser('~/.local/bin/aaron')
EDITOR_PROFILE = 'Blog'

try:
    import markdown
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


def build(source=SOURCE, template=TEMPLATE):
    with open(source, encoding='utf-8') as f:
        content = render_content(f.read())
    with open(template, encoding='utf-8') as f:
        page = f.read()
    return (page.replace('{{ content }}', content)
                .replace('{{ year }}', str(date.today().year)))


def main():
    parser = argparse.ArgumentParser(
        description='Build the homepage from Markdown.')
    parser.add_argument('-o', '--output', default=OUTPUT,
                        help='where to write the page; "-" is stdout '
                             '(default: root/index.html)')
    parser.add_argument('--edit', action='store_true',
                        help='open about.md in Aaron before building')
    args = parser.parse_args()

    if args.edit:
        subprocess.run([EDITOR, '--profile', EDITOR_PROFILE, SOURCE],
                       stdout=subprocess.DEVNULL, check=True)

    page = build()
    if args.output == '-':
        sys.stdout.write(page)
    else:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(page)
        print(args.output, file=sys.stderr)


if __name__ == '__main__':
    main()
