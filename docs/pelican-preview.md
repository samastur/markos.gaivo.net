# Pelican preview tool

`preview_pelican.py` renders a complete HTML page using the site's settings,
theme, readers and enabled plugins. It runs a normal Pelican lifecycle in a
fresh subprocess, including finalization hooks, then returns the selected page.
It does not install dependencies or run `uv sync`.

```sh
# Input file -> stdout
./preview_pelican.py articles/content/homeconf.md

# Input file -> destination (parent directory must already exist)
./preview_pelican.py articles/content/homeconf.md -o /tmp/preview.html

# Unsaved buffer -> stdout, retaining the original logical filename
cat articles/content/homeconf.md | ./preview_pelican.py --source-path homeconf.md

# Another project, explicit interpreter, page rather than article
./preview_pelican.py /work/site/content/pages/about.md \
  --settings /work/site/publishconf.py --venv /work/site/.venv --kind page

# Site-wide dependencies, such as links to other source documents
./preview_pelican.py articles/content/homeconf.md --full-context

# Override settings (values are JSON)
./preview_pelican.py post.md --set 'SITEURL="http://localhost:8000/articles"' \
  --set 'DEFAULT_METADATA={"status":"published"}' -o /tmp/preview.html
```

## Debugging from the command line

The script is executable; call it directly from the repository root or by its
absolute path from another directory. No activation or installation is required.
Use `--help` to list all options.

```sh
./preview_pelican.py articles/content/homeconf.md --debug --keep-build -o /tmp/preview.html
```

`--debug` sends the selected interpreter's build command, working directory,
settings path, Pelican debug logging and error tracebacks to stderr. Stdout stays
reserved for HTML. `--keep-build` prints and preserves the temporary directory
on success or failure, including staged content, generated output and `job.json`.
Delete this directory manually when finished; it contains a copy of your content.
Without this flag, temporary files are cleaned up automatically.

For a Python debugger, use the interpreter and worker arguments printed by
`--debug`, inserting `-m pdb` before the script path, and run from the printed
working directory. Use a fresh ordinary invocation when you want a new build;
replaying a retained job requires removing its staged `content` directory first.

## Defaults and overrides

Run `./preview_pelican.py --help` for all options.

- Input defaults to stdin (`-`). Output defaults to stdout (`-`). Diagnostics,
  including plugin prints and build errors, go to stderr. Exit status is zero
  on success and nonzero on failure. File output is replaced atomically only
  after a successful build; existing output survives build errors.
- Settings default to this repository's `articles/publishconf.py`, relative to
  the script, independently of your shell's working directory. `--settings`
  replaces this. The build working directory defaults to the settings directory;
  `--cwd` overrides it for configurations/plugins that depend on working directory.
- Interpreter discovery checks `.venv/bin/python` beside the settings file,
  then in its parent directory, then uses the launcher's Python. `--python`
  chooses an executable directly; `--venv` chooses an environment. An environment
  without Pelican fails with a diagnostic, without installing anything. The
  launcher requires Python 3.9+; the build interpreter must support the installed
  Pelican (currently Python 3.11+ for Pelican 4.12).
- The content root comes from configured `PATH`; `--content-root` overrides it.
  Relative paths in Pelican settings follow Pelican's own resolution rules.
  Explicit CLI filesystem paths are relative to the invoking directory.
- A file inside the content root retains its relative path. An external file
  uses its basename. Stdin uses `preview.md`. `--source-path` overrides this
  logical path, including its extension, which selects the Pelican reader.
  Absolute paths and `..` components are rejected. Supply the original path
  for an unsaved buffer to preserve folder categories and relative references.
- `--kind auto` treats paths under configured `PAGE_PATHS` as pages, and other
  inputs as articles. `--kind article` or `--kind page` overrides classification
  in restricted builds. With `--full-context`, configured article/page paths
  and exclusions control discovery; ensure the logical source is included.
- `--set KEY=JSON` overrides any Pelican setting except the isolation settings
  listed below. For example, override `THEME`, `PLUGINS`, `IGNORE_FILES`, reader
  settings, or default metadata. Explicit source metadata still takes precedence
  over default metadata: the tool does not silently rewrite titles, dates,
  slugs, statuses, or future publication dates. Missing required metadata fails.
- By default, only the selected source is processed as an article/page.
  `--full-context` retains configured content discovery for cross-post links,
  related posts, translations, and other plugins requiring the whole site.
- `--rendered-path` explicitly selects a path within temporary output when a
  custom plugin does not emit Pelican's normal `content_written` signal or
  generates multiple candidate pages. Normally output is discovered from that
  signal, including custom save paths and drafts, without guessing the slug.
- `--temp-dir` overrides the system temporary directory; `--timeout` overrides
  the 60-second build timeout. The temporary build is removed on completion unless `--keep-build` is set.

## Isolation and fidelity

The tool copies the content tree (including assets and dereferenced symlinks)
into temporary storage, then overlays the supplied input. Original sources are
not edited. This can cost time and disk space for large content trees. Production
output and caches are not used: `OUTPUT_PATH`, `CACHE_PATH`, `CACHE_CONTENT`,
`LOAD_CONTENT_CACHE`, `DELETE_OUTPUT_DIRECTORY`, and `STATIC_CREATE_LINKS` are
managed by the tool. The staged `PATH` replaces the original during generation.
Restricted builds also replace `ARTICLE_PATHS` and `PAGE_PATHS`. Other settings,
including feeds and plugins, remain enabled to preserve their effects on HTML.

Configuration and plugins are trusted executable Python. This is build-output
isolation, **not a security sandbox**: arbitrary plugins can access external
paths or services. Plugins depending on absolute source locations can also
behave differently under staging. Logged Pelican errors fail the preview instead
of returning potentially incomplete HTML; warnings remain diagnostics.

The result includes the theme's full page. Navigation, aggregate lists and
sitemaps reflect the restricted content unless `--full-context` is used. Assets
are processed during the build, but only the HTML is exported; this is not a
self-contained offline page. Serve existing assets at the paths expected by the
theme. This site's theme uses `/articles/` paths and an external Isso comments
script. Relative links resolve against the URL at which the preview is served,
not the CLI output filename. Use an iframe to isolate the theme from editor CSS.

## Validation

```sh
articles/.venv/bin/python -m unittest discover -s tests -v
```

Integration tests exercise file/stdin parity, custom generated paths, generator
and finalization plugins, draft pages, full-context rendering, path validation,
and preservation of sources and existing output on failure. They use only the
standard library and the already-installed Pelican environment.
