from datetime import date
import re

AUTHOR = 'Marko Samastur'
SITENAME = 'A notch above a monkey'
SITEURL = 'http://markos.gaivo.net/articles'

PATH = 'content'

TIMEZONE = 'Europe/Ljubljana'

# Used by the theme's footer copyright notice.
CURRENT_YEAR = date.today().year

DEFAULT_LANG = 'en'
# Posts in another language say so with "Lang: sl" (ISO 639-1 code) in their
# metadata. Pelican would publish them as <slug>-<lang>.html; keep their URLs.
ARTICLE_LANG_URL = '{slug}.html'
ARTICLE_LANG_SAVE_AS = '{slug}.html'
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


def minify_css(css):
    """Strip comments and needless whitespace from the theme's stylesheet.

    Only meant for our own home.css: it keeps spaces inside strings and
    before ":" (descendant combinator vs. pseudo-class), so it is safe there.
    """
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{};,]|>=?)\s*', r'\1', css)
    css = re.sub(r':\s+', ':', css)
    return css.replace(';}', '}').strip()


def minify_js(js):
    """Drop whole-line // comments, indentation and blank lines."""
    lines = (line.strip() for line in js.splitlines())
    return '\n'.join(line for line in lines
                     if line and not line.startswith('//'))


# The theme inlines its stylesheet and script through these filters
# (templates/head.html, footer.html); build_homepage.py uses them too, for the
# homepage and the error pages.
JINJA_FILTERS = {'minify_css': minify_css, 'minify_js': minify_js}


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
