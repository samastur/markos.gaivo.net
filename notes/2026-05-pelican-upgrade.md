# Pelican upgrade — May 2026

The blog under `articles/` was originally built with Pelican 4.0.1 on
Python 2/3 with a vendored `pelican-plugins` checkout. This note records what
changed when it was brought up to current Pelican on Python 3.13, managed by
[uv](https://docs.astral.sh/uv/).

## What changed

| Area | Before | After |
| --- | --- | --- |
| Python | 2/3 (implicit) | 3.13 (`uv python pin`) |
| Pelican | 4.0.1 | 4.12.x |
| Plugin loading | `PLUGIN_PATHS = ['pelican-plugins']` (a since-removed Git submodule) | PyPI packages under the `pelican.plugins.*` namespace |
| simple_footnotes | vendored | `pelican-simple-footnotes` |
| sitemap | vendored | `pelican-sitemap` |
| Env / deps | `requirements.txt` + global `pip` | `pyproject.toml` + `uv.lock` |
| Dev server | `develop_server.sh` (custom PID juggling, `python -m pelican.server`) | `pelican --listen --autoreload` |
| Markdown date fallback | `DEFAULT_DATE = 'fs'` | unset (every article has explicit `Date:`; see note below) |

## Output parity

The goal was to keep the generated site byte-identical to the previous build.
After tuning `pelicanconf.py`, **1,139 of 1,226 output files match exactly**.
The remaining 87 differences are all driven by upstream library changes that
cannot be undone without forking the libraries:

- **Atom feeds (62 files in `feeds/`)** — `feedgenerator` now emits
  self-closing XML tags (`<link href="…"/>` instead of
  `<link …></link>`), and Pelican now lists the article's *category* alongside
  its tags as `<category term="…"/>` entries. Same data, more canonical XML.
- **Code blocks (~15 paginated/category/tag/author pages)** — Pygments now
  wraps highlighted blocks in `<pre><code>…</code></pre>`, emits explicit
  `<span class="w">` whitespace tokens, and uses a finer-grained token
  taxonomy (e.g. `class="k"` keyword vs. the older `class="nt"` name-tag).
- **Footnotes (~5 articles)** — `pelican-simple-footnotes` now quotes all
  HTML attributes and uses the U+21A9 ↩ glyph followed by U+FE0E (text
  presentation selector). The previous build emitted unquoted attributes and
  a bare ↩.
- **`tags.html` + one tag page** — Pelican's slugifier no longer leaks the
  literal text "amp" out of `&amp;`; the tag formerly known as
  `compensation-amp.html` is now `compensation.html`.
- **`sitemap.xml`** — `pelican-sitemap` 1.x adds an `xmlns:xhtml` namespace
  declaration, sorts URLs alphabetically (the old plugin emitted indexes
  first, then articles), and uses the build time as `<lastmod>` for index
  pages instead of a baked-in 2022 timestamp.
- **`archive.html`** — single trailing blank line dropped.

The `pelicanconf.py` `SITEMAP['exclude']` regex list was extended to keep
the sitemap to the same set of URLs as before (paginated `index*.html`,
the `authors.html` index, and paginated `author/markos<N>.html` are all
excluded so the URL list matches the historical sitemap exactly).

## A note on `DEFAULT_DATE`

The old config had `DEFAULT_DATE = 'fs'` as a fallback for articles missing
a `Date:` header. Every article in `articles/content/` already has an
explicit `Date:`, so the fallback was unused. Pelican ≥ 4.5 also populates
`article.modified` from the file mtime when `DEFAULT_DATE = 'fs'`, which
caused the icecream theme to render a spurious "Modified on …" line on every
article. The setting is therefore omitted; if you ever want a filesystem
fallback again, restore it but be aware of the `modified` side-effect (e.g.
guard `{% if article.modified %}` with `and article.modified != article.date`
in the theme).
