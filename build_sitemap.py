#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write root/sitemap.xml (sitemaps.org protocol 0.9) for markos.gaivo.net.

It lists the homepage and every published blog post. Posts are read from
articles/content with Pelican's own reader and the publish settings, so
slugs, URLs and the default status match the generated site. A post's
<lastmod> is its Modified metadata if it has one, otherwise its Date. The
homepage's <lastmod> is the modification time of homepage/about.md.

Examples:
    build_sitemap.py            # write root/sitemap.xml
    build_sitemap.py -o -       # print it instead
"""

from datetime import datetime
from os.path import abspath, dirname, getmtime, join
from xml.sax.saxutils import escape
import argparse
import os
import sys

THIS_DIR = abspath(dirname(__file__))
ARTICLES_DIR = join(THIS_DIR, 'articles')
CONTENT_DIR = join(ARTICLES_DIR, 'content')
HOMEPAGE_SOURCE = join(THIS_DIR, 'homepage', 'about.md')
OUTPUT = join(THIS_DIR, 'root', 'sitemap.xml')
HOMEPAGE_URL = 'https://markos.gaivo.net/'

try:
    from pelican.contents import Article
    from pelican.readers import Readers
    from pelican.settings import read_settings
except ImportError:
    # Not running inside the articles uv env, so re-exec through it.
    os.execvp('uv', ['uv', 'run', '--project', ARTICLES_DIR,
                     'python', abspath(__file__)] + sys.argv[1:])


def published_posts():
    # publishconf.py imports pelicanconf from the current directory.
    os.chdir(ARTICLES_DIR)
    settings = read_settings(join(ARTICLES_DIR, 'publishconf.py'))
    readers = Readers(settings)
    extensions = tuple('.' + ext for ext in readers.extensions)
    site_url = settings['SITEURL'].rstrip('/')

    for name in sorted(os.listdir(CONTENT_DIR)):
        if not name.endswith(extensions):
            continue
        post = readers.read_file(CONTENT_DIR, name, content_class=Article,
                                 context={})
        if post.status != 'published':
            continue
        lastmod = getattr(post, 'modified', None) or post.date
        yield site_url + '/' + post.url, lastmod


def url_entry(loc, lastmod):
    return ('  <url>\n'
            f'    <loc>{escape(loc)}</loc>\n'
            f'    <lastmod>{lastmod.isoformat(timespec="seconds")}</lastmod>\n'
            '  </url>\n')


def build():
    homepage_mtime = datetime.fromtimestamp(getmtime(HOMEPAGE_SOURCE)).astimezone()
    entries = [url_entry(HOMEPAGE_URL, homepage_mtime)]
    entries += [url_entry(loc, lastmod) for loc, lastmod in published_posts()]
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + ''.join(entries) +
            '</urlset>\n')


def main():
    parser = argparse.ArgumentParser(
        description='Build sitemap.xml for the homepage and published posts.')
    parser.add_argument('-o', '--output', default=OUTPUT,
                        help='where to write the sitemap; "-" is stdout '
                             '(default: root/sitemap.xml)')
    args = parser.parse_args()

    sitemap = build()
    if args.output == '-':
        sys.stdout.write(sitemap)
    else:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(sitemap)
        print(f'{args.output}: {sitemap.count("<url>")} URLs', file=sys.stderr)


if __name__ == '__main__':
    main()
