AUTHOR = 'Marko Samastur'
SITENAME = 'A notch above a monkey'
SITEURL = 'http://markos.gaivo.net/articles'

PATH = 'content'

TIMEZONE = 'Europe/Ljubljana'

DEFAULT_LANG = 'en'
# Every article carries explicit Date metadata, so a 'fs' fallback is unnecessary.
# In Pelican >= 4.5 'fs' also populates `modified` from the file mtime, which would
# add a spurious "Modified on" line to every article — keep it unset to preserve
# the historical output exactly.

# Feed generation is usually not desired when developing
FEED_DOMAIN = '/articles'
FEED_ALL_ATOM = 'feeds/atom.xml'
FEED_ALL_RSS = 'feeds/rss.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_MAX_ITEMS = 10

# Blogroll
LINKS = (
    #('Python.org', 'http://python.org/'),
)

DEFAULT_PAGINATION = 3

PLUGINS = [
    'pelican.plugins.simple_footnotes',
    'pelican.plugins.sitemap',
]

THEME = '../pelican_themes/icecream'


DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    },
    # Excludes are regex patterns matched against the URL (relative to the
    # output dir). Old pelican-sitemap silently dropped paginated indexes and
    # the secondary author pages — replicate that here.
    'exclude': [
        r'^tag/',
        r'^category/',
        r'^author/markos\d+\.html$',
        r'^authors\.html$',
        r'^index\d+\.html$',
    ]
}
