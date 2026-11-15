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

## Homepage

The homepage text lives in `homepage/about.md`; `homepage/template.html` holds
the rest of the page, with `{{ content }}` and `{{ year }}` placeholders.
`build_homepage.py` renders it into `root/index.html` (`--edit` opens the
Markdown in Aaron first, `-o -` prints to stdout).

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
