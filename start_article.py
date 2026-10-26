#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from os.path import abspath, dirname, join, exists, expanduser
import os
import shutil
import subprocess
import sys

THIS_DIR = abspath(dirname(__file__))
ARTICLES_DIR = join(THIS_DIR, 'articles')
CONTENT_DIR = join(ARTICLES_DIR, 'content')

try:
    from pelican.settings import DEFAULT_CONFIG
    from pelican.utils import slugify
except ImportError:
    # Not running inside the articles uv env, so re-exec through it.
    os.execvp('uv', ['uv', 'run', '--project', ARTICLES_DIR,
                     'python', abspath(__file__)] + sys.argv[1:])

ARTICLE_HEADER = '''\
Title: {title}
Date: {date}
Author: markos
Category:
Slug: {slug}
Status: draft
Tags:

'''

EDITOR = shutil.which('aaron') or expanduser('~/.local/bin/aaron')
EDITOR_PROFILE = 'Blog'


def create_slug(title):
    slug = base_slug = slugify(
        title, regex_subs=DEFAULT_CONFIG['SLUG_REGEX_SUBSTITUTIONS'])
    filename = join(CONTENT_DIR, slug + '.md')
    count = 1
    while exists(filename):
        slug = "{0}-{1}".format(base_slug, count)
        filename = join(CONTENT_DIR, slug + '.md')
        count += 1
    return (slug, filename)


def create_draft(filename, metadata):
    header = ARTICLE_HEADER.format(**metadata)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(header)


def open_editor(filename):
    subprocess.run([EDITOR, '--profile', EDITOR_PROFILE, filename],
                   stdout=subprocess.DEVNULL, check=True)


def main(title):
    now = datetime.now()
    date = now.isoformat().replace("T", " ").split(".")[0]
    metadata = {
        'title': title,
        'date': date
    }
    slug, filename = create_slug(title)
    metadata['slug'] = slug
    create_draft(filename, metadata)
    print(filename)
    open_editor(filename)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('You have to pass title of the article as first parameter')
        sys.exit(1)
    title = sys.argv[1]
    main(title)
