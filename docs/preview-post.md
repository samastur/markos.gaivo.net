# Post preview tool

`preview_post.py` renders a single post exactly as Pelican would render it on
the site, without building the rest of the site. It is meant for quick
previews while writing or editing, e.g. from an editor or another tool.

Pelican itself does the work: the post is read with the configured reader,
processed by the enabled plugins and rendered with the theme's template and
Pelican's writer. Only the generation of all other pages (index, tags,
categories, feeds, other posts) is skipped. A preview takes about 0.3 s, most
of which is loading Pelican, and does not grow with the size of the blog.

```sh
# Post -> stdout
./preview_post.py articles/content/resurrection.md

# Post -> file
./preview_post.py articles/content/resurrection.md -o /tmp/preview.html

# Unsaved buffer on stdin, as if it were content/my-draft.md
cat my-draft.md | ./preview_post.py --name my-draft.md -o /tmp/preview.html

# Render with the production settings
./preview_post.py articles/content/resurrection.md \
  --settings articles/publishconf.py

# Override settings (values are parsed as JSON when possible)
./preview_post.py articles/content/resurrection.md \
  --setting SITEURL='"http://localhost:8000"' --setting TYPOGRIFY=true

# Render as a page instead of an article
./preview_post.py --page --name pages/about.md < about.md
```

The script is executable and can be run by its full path from any directory.
It does not need an activated virtual environment and installs nothing.

## Options

| Option | Default | Meaning |
|---|---|---|
| `input` | `-` (stdin) | Post to render. |
| `-o`, `--output` | `-` (stdout) | File to write the rendered page to. |
| `--name` | see below | Path of the post relative to the content directory. |
| `--page` | off | Render as a page instead of an article. |
| `--project` | `articles/` next to the script | Pelican project whose virtual env is used. |
| `--settings` | `PROJECT/pelicanconf.py` | Pelican settings file. |
| `--content` | `PATH` from the settings | Content directory. |
| `--setting KEY=VALUE` | none | Override a Pelican setting; can be repeated. |
| `--python` | `PROJECT/.venv/bin/python` | Interpreter with Pelican installed. |
| `-q`, `--quiet` | off | Only report errors, not Pelican warnings. |

Run `./preview_post.py --help` for the full list.

### The post's name

Pelican uses a post's location inside the content directory to resolve
relative `{filename}` links, extract path metadata (`PATH_METADATA`,
`FILENAME_METADATA`) and pick the reader from the file extension. `--name`
sets that location:

- An input file inside the content directory uses its own path.
- An input file elsewhere uses its file name, as if it were placed at the top
  of the content directory.
- Stdin uses `preview.md`.

Give stdin input a realistic `--name`, especially if it links to other posts
with relative paths or isn't Markdown.

## Output and errors

The rendered page goes to stdout or the `--output` file; nothing else is
written to stdout. Pelican's warnings and errors go to stderr. The exit status
is 0 on success and 1 on failure, for example when the input file is missing,
no reader handles its extension, a `--setting` is malformed, or Pelican
rejects the post (such as a missing `Date:` on an article).

Nothing is written to the project: the page is rendered into a temporary
directory, which is deleted afterwards, and Pelican's content caching is
turned off for the preview.

## Virtual environment

If Pelican can't be imported by the Python running the script, the script
re-runs itself with `PROJECT/.venv/bin/python` (or `--python`). If that
interpreter doesn't exist, it falls back to `uv run --project PROJECT`.

## How it works

The tool runs Pelican's own `ArticlesGenerator` (or `PagesGenerator` with
`--page`) with a file list containing only the input post, so reading,
metadata processing, taxonomy and plugin signals all follow Pelican's normal
code path. It then sends the signals a full build sends after generating
content (`all_generators_finalized`, `article_generator_write_article` or
`page_generator_write_page`) and writes the post with Pelican's `Writer` and
the post's template.

Links to other content are resolved lazily. Pelican looks up `{filename}`,
`{static}` and `{attach}` targets in its context; the preview fills those
lookups on demand by reading only the linked files. Links therefore point to
the same URLs as on the real site without reading the whole content directory.

## Limitations

- Plugins that only act when the whole site is finished (the `finalized`
  signal, used e.g. by the sitemap plugin), or that write extra files after
  the articles (`article_writer_finalized`), are not run. They don't change
  the post's own page.
- Templates see only the previewed post in site-wide lists such as
  `articles`, `tags` and `categories`, so navigation or sidebars built from
  them show less than on the real site.
- With `DEFAULT_DATE = 'fs'` in the settings, posts without a `Date:` fail to
  render from stdin or from outside the content directory, unless `--name`
  points to an existing file there. Pelican takes the date from the
  modification time of the file at that location. This site sets dates
  explicitly, so it is not affected.

## Verification

With `articles/publishconf.py`, previews of all 363 posts were byte-for-byte
identical to the pages from a full `pelican` build, including posts with
`{filename}`/`{static}` links and footnotes.
