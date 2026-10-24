# markos.gaivo.net

Personal site of Marko Samastur. The blog under `articles/` is a static site
built with [Pelican](https://getpelican.com/); the rest of the repo holds
older site bits (`root/`), the CV pipeline (`cv/`, `build_cv.py`), and the
WordPress dump that seeded the blog.

## Articles (Pelican blog)

### Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) (>= 0.4)
- Make (optional, for the convenience targets)

uv handles Python and the virtualenv itself — no separate Python install is
needed. The Python version is pinned in `articles/.python-version`.

### One-time setup

```sh
cd articles
uv sync
```

`uv sync` reads `pyproject.toml` + `uv.lock` and creates `.venv/` with all
dependencies (Pelican, Markdown, Typogrify, `pelican-sitemap`,
`pelican-simple-footnotes`).

### Building

```sh
cd articles

# Development build (absolute SITEURL)
make html

# Production build (RELATIVE_URLS=True, deletes output dir first)
make publish

# Live preview with auto-rebuild on content changes
make devserver         # http://localhost:8000
make devserver PORT=8080

# Plain server over an existing build
make serve
```

The `make` targets shell out to `uv run pelican …`, so you can also drive
Pelican directly:

```sh
uv run pelican content -o output -s pelicanconf.py            # dev
uv run pelican content -o output -s publishconf.py            # publish
uv run pelican --listen --autoreload content -o output -s pelicanconf.py
```

### Adding dependencies

```sh
cd articles
uv add some-pelican-plugin
uv lock --upgrade        # bump everything to latest compatible
```

## CV

`build_cv.py` builds the CV PDF; deps live in the top-level
`requirements.txt` (CairoSVG, WeasyPrint, etc.).

## Notes

Background and design notes (e.g. the 2026 Pelican upgrade) live in
[`notes/`](notes/).

## Tool documentation

See [tools documentation](docs/README.md) for descriptions and usage.
