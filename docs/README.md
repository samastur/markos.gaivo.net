# Tools documentation

## Pelican preview

`preview_pelican.py` renders an input file or stdin into an HTML preview using
the blog’s Pelican theme and enabled plugins. It uses the local virtual
environment and isolated temporary builds, with output to stdout or a file.
See the [CLI documentation](pelican-preview.md) for usage and options.

## Post preview

`preview_post.py` renders a single post from a file or stdin exactly as
Pelican would on the site, using its theme and enabled plugins, but without
building any other pages, so a preview takes about 0.3 s. It picks up the
local virtual environment and writes to stdout or a file. See the
[CLI documentation](preview-post.md) for usage and options.

## Homepage and error pages

The homepage text lives in `homepage/about.md`; `homepage/template.html` holds
the rest of the page. `build_homepage.py` renders it into `root/index.html`,
and `homepage/404.html` and `homepage/500.html` into `root/` as well (`--edit`
opens the Markdown in Aaron first, `-o -` prints the homepage to stdout).

The templates are Jinja, rendered with the blog's settings and theme, so they
include the theme's `head.html` and `footer.html` and look exactly like the
blog, dark mode included. Edit the shared parts in the theme, not here.

## Theme, stylesheet and dark mode

The only stylesheet is `pelican_themes/icecream/static/css/home.css`. It is not
linked but inlined into every page (blog, homepage, error pages) by
`templates/head.html`, minified on the way by the `minify_css` filter defined
in `articles/pelicanconf.py`; there is no `.min.css` to keep in sync. After
changing it, rebuild the blog (`make publish`) and the root pages
(`build_homepage.py`, or just `deploy_root.sh`).

Light and dark themes use the same four colours, swapped; everything that
differs is a custom property at the top of `home.css`. Pages follow the
system's light/dark preference. The sun|moon switch in the footer
(`templates/theme.js`) highlights the theme on screen and overrides the system
for the site, following
[Lea Verou's recommendation](https://lea.verou.me/blog/2026/dark-mode-toggles/):
choosing the other theme stores `light` or `dark` in `localStorage.theme` only
when that differs from the system, and clears it when it matches, so the site
follows the system again.

Switching animates through a view transition: the footer logo fades out, the
page cross-fades to the other colours, then the new logo fades in. The logo
images have the footer colour baked in, which is why they sit the cross-fade
out. The timing is set by `--logo-fade` and `--theme-fade` in `home.css`.
Browsers without view transitions, and readers who prefer reduced motion,
get an instant switch, as do changes coming from the system or another tab.

## Posts in Slovenian

Mark a post written in Slovenian with `Lang: sl` in its metadata (`sl` is the
ISO 639-1 code; `si` would be Sinhala). The page then gets `lang="sl"`, which
browsers use for hyphenation, spell checking and screen reader voices.
`pelicanconf.py` sets `ARTICLE_LANG_URL`/`ARTICLE_LANG_SAVE_AS` so such a post
keeps its usual URL instead of Pelican's default `<slug>-sl.html`.

`deploy_root.sh` rebuilds the homepage and rsyncs `root/` to the web root on
the server, uploading `htaccess` as `.htaccess`. The blog's `articles/`
directory is excluded and never touched. Pass `-n` for a dry run; remote files
are only removed when `--delete` is given.

## Sitemap

`build_sitemap.py` writes `root/sitemap.xml` with the homepage and every
published blog post. Posts are read with Pelican's own reader and the publish
settings, so URLs and the default `published` status match the real site.
A post's `lastmod` is its `Modified` metadata, falling back to `Date`; the
homepage's is the modification time of `homepage/about.md`. `deploy_root.sh`
regenerates it on every deploy, so the file itself isn't tracked in git.
Submit `https://markos.gaivo.net/sitemap.xml` in Google Search Console.
