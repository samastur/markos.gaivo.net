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
