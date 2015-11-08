#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marko Samastur'
SITENAME = u'A notch above a monkey'
SITEURL = 'http://markos.gaivo.net'

PATH = 'content'

TIMEZONE = 'Europe/Ljubljana'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = '/articles'
FEED_ALL_ATOM = 'feeds/atom.xml'
FEED_ALL_RSS = 'feeds/rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_MAX_ITEMS = 10

# Blogroll
LINKS = (
    #('Python.org', 'http://python.org/'),
)

DEFAULT_PAGINATION = 3

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['simple_footnotes']

THEME = '../pelican_themes/icecream'


DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
