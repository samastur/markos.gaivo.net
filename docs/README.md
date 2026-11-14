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
