#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from os.path import abspath, dirname, join, exists
from slugify import slugify
from subprocess import call, PIPE
import sys

THIS_DIR = abspath(dirname(__file__))
CONTENT_DIR = join(THIS_DIR, 'articles', 'content')

ARTICLE_HEADER = '''\
Title: {title}
Date: {date}
Author: markos
Category:
Slug: {slug}
Status: draft
Tags:

'''

EDITOR = '/usr/local/bin/markdown'


def create_slug(title, dir):
    slug = base_slug = slugify(title)
    filename = join(CONTENT_DIR, slug + '.md')
    count = 1
    while exists(filename):
        slug = "{0}-{1}".format(base_slug, count)
        filename = join(CONTENT_DIR, slug + '.md')
        count += 1
    return (slug, filename)


def create_draft(filename, metadata):
    header = ARTICLE_HEADER.format(**metadata)
    with open(filename, 'w') as f:
        f.write(header)


def open_editor(filename):
    cmd = "{0} {1}".format(EDITOR, filename)
    call(cmd, shell=True, stdout=PIPE)


def main(title):
    now = datetime.now()
    date = now.isoformat().replace("T", " ").split(".")[0]
    metadata = {
        'title': title,
        'date': date
    }
    slug, filename = create_slug(title, CONTENT_DIR)
    metadata['slug'] = slug
    create_draft(filename, metadata)
    open_editor(filename)


if __name__ == '__main__'
    if len(sys.argv) != 2:
        print 'You have to pass title of the article as  first parameter'
        sys.exit(1)
    title = sys.argv[1]
    main(title)
