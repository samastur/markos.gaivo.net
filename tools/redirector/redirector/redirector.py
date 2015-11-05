#!/usr/bin/env python

# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import argparse
import os


def post_redirects(filename, prefix=""):
    redirects = []
    prefix = "" if not prefix else "/" + prefix

    with open(filename, 'r') as f:
        for line in f.readlines():
            pid, slug = line.strip().split('\t')
            redirects.append('Redirect 301 /blog/?p={} /articles/{}{}.html'.format(pid, prefix, slug))
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
