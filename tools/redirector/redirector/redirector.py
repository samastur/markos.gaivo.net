#!/usr/bin/env python

# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import argparse
import os


OLD_CATEGORIES = {
    3: "catchall",
    9: "company",
    39: "django",
    5: "general-development",
    1: "javascript",
    6: "linux",
    170: "opendata",
    2: "python",
    8: "spletne-urice",
    7: "ui",
    4: "web",
}


def categories_redirects(redirects):
    # Redirect each category and its subpages to new main one because subpages
    # will change over time
    for cat_id, slug in OLD_CATEGORIES.items():
        # Some of these actually don't exist as some categories were never used
        # alone
        redirects.append('Redirect 301 /blog/?cat={} /articles/category/{}.html'.format(cat_id, slug))
        redirects.append('RedirectMatch 301 /blog/?cat={}&paged=\d*$ /articles/category/{}.html'.format(cat_id, slug))


def feeds_redirects(redirects):
    feed_types = ('atom', 'rss')

    for feed_type in feed_types:
        # First redirect global ones
        redirects.append('Redirect 301 /blog/?feed={} /articles/feeds/{}.xml'.format(feed_type, feed_type))

        for cat_id, slug in OLD_CATEGORIES.items():
            # Redirect category feeds to new ones...
            redirects.append(
                'Redirect 301 /blog/?feed={}&cat={} /articles/feeds/{}.atom.xml'.format(feed_type, cat_id, slug))
            redirects.append(
                'Redirect 301 /blog/?feed={}&amp;cat={} /articles/feeds/{}.atom.xml'.format(feed_type, cat_id, slug))
            redirects.append(
                'Redirect 301 /blog/?cat={}&feed={} /articles/feeds/{}.atom.xml'.format(cat_id, feed_type, slug))
            redirects.append(
                'Redirect 301 /blog/?cat={}&amp;feed={} /articles/feeds/{}.atom.xml'.format(cat_id, feed_type, slug))
            redirects.append(
                'Redirect 301 /blog/?amp;cat={}&feed={} /articles/feeds/{}.atom.xml'.format(cat_id, feed_type, slug))

        # ...and send any other feed request to new global
        redirects.append('RedirectMatch 301 /blog/?feed={}&.*$ /articles/feeds/{}.xml'.format(feed_type, feed_type))


def index_redirects(redirects):
    # Redirect all old index pages to main one since they get incorrect
    # over time.
    redirects.append('RedirectMatch 301 /blog/?paged=.*$ /articles/')


def post_redirects(filename, prefix=""):
    redirects = []
    prefix = "" if not prefix else "/" + prefix

    with open(filename, 'r') as f:
        # Create redirects for posts (articles)...
        for line in f.readlines():
            pid, slug = line.strip().split('\t')
            redirects.append('Redirect 301 /blog/?p={} /articles/{}{}.html'.format(pid, prefix, slug))

        # Also for categories...
        categories_redirects(redirects)

        # And feeds...
        feeds_redirects(redirects)

        # And main index pages...
        index_redirects(redirects)

        # Pass through request to code
        redirects.append('RewriteCond %{REQUEST_URI} !^/blog/code/.*$')

        # Anything else should be redirected to main articles index page
        # redirects.append('RedirectMatch 301 ^/blog/?.*$ /articles/')

    return "\n".join(redirects)


def main():
    parser = argparse.ArgumentParser(
        description="Transform id_slugs.tsv files into .htaccess file with "
                    "permanent redirects.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(dest='input', help='The input file to read')
    parser.add_argument(
        '-o', '--output', dest='output', default='htaccess',
        help='Output path')

    args = parser.parse_args()

    core_redirects = post_redirects(args.input, "")
    if os.path.exists(args.output):
        error = "This file already exists: " + args.output
        exit(error)

    with open(args.output, 'w') as fs:
        fs.write(core_redirects)
