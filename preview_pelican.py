#!/usr/bin/env python3
"""Render one source through the project's real Pelican build and plugins.

The launcher uses only the standard library; Pelican runs in a fresh interpreter.
Configuration and plugins are trusted executable Python, not sandboxed code.
"""
import argparse
import contextlib
import json
import logging
import os
from pathlib import Path
import shutil
import shlex
import subprocess
import sys
import tempfile
import traceback

ROOT = Path(__file__).resolve().parent
# These must remain isolated even when production settings enable caching/deletion.
ISOLATED = {"OUTPUT_PATH", "CACHE_PATH", "CACHE_CONTENT", "LOAD_CONTENT_CACHE",
            "DELETE_OUTPUT_DIRECTORY", "STATIC_CREATE_LINKS"}


def relative_path(value):
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError("source/output-relative paths must be nonempty and contain no '..'")
    return path


def worker(job_path):
    # Redirect even prints from settings/plugins away from the HTML output channel.
    with contextlib.redirect_stdout(sys.stderr):
        from pelican import Pelican, signals
        from pelican.settings import read_settings

        job = json.loads(Path(job_path).read_text())
        if job.get("debug"):
            logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)
        work = Path(job["work"])
        settings = read_settings(job["settings"], override=job["overrides"])
        original = Path(settings["PATH"]).resolve()
        if work.is_relative_to(original):
            raise ValueError("temporary directory must be outside the content root")
        source = Path(job["input"]) if job["input"] else None
        if job["source_path"]:
            relative = relative_path(job["source_path"])
        elif source:
            relative = source.relative_to(original) if source.is_relative_to(original) else Path(source.name)
        else:
            relative = Path("preview.md")
        staged = work / "content"
        if original.is_dir():
            # Copies, not links: plugins cannot mutate originals through the staging tree.
            shutil.copytree(original, staged)
        else:
            staged.mkdir()
        target = staged / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if source:
            shutil.copy2(source, target)
        else:
            target.write_bytes((work / "stdin").read_bytes())

        kind = job["kind"]
        if kind == "auto":
            kind = "article"
            for entry in settings["PAGE_PATHS"]:
                page_path = Path(entry)
                if relative == page_path or page_path in relative.parents:
                    kind = "page"
                    break
        if not job["full_context"]:
            settings["ARTICLE_PATHS"] = [str(relative)] if kind == "article" else []
            settings["PAGE_PATHS"] = [str(relative)] if kind == "page" else []
        output = work / "output"
        settings.update(PATH=str(staged), OUTPUT_PATH=str(output),
                        CACHE_PATH=str(work / "cache"), CACHE_CONTENT=False,
                        LOAD_CONTENT_CACHE=False, DELETE_OUTPUT_DIRECTORY=False,
                        STATIC_CREATE_LINKS=False)
        written = set()

        def record(path, context):
            content = context.get("article") or context.get("page")
            if content is not None and getattr(content, "source_path", None):
                if Path(content.source_path).resolve() == target.resolve():
                    written.add(Path(path).resolve())

        signals.content_written.connect(record)
        errors = []

        class BuildErrors(logging.Handler):
            def emit(self, record):
                if record.levelno >= logging.ERROR:
                    errors.append(record.getMessage())

        logging.getLogger().addHandler(BuildErrors())
        Pelican(settings).run()
        if errors:
            raise ValueError("Pelican reported errors: " + "; ".join(errors))
        if job["rendered_path"]:
            result = output / relative_path(job["rendered_path"])
        elif len(written) == 1:
            result = written.pop()
        else:
            raise ValueError(
                f"expected one rendered page for {relative}, found {len(written)}; "
                "check metadata, status, reader and exclusions, or use --rendered-path"
            )
        if not result.resolve().is_relative_to(output.resolve()):
            raise ValueError("rendered page is outside the isolated output directory")
        # Read AFTER finalized hooks, including plugins that rewrite HTML on disk.
        (work / "result").write_bytes(result.read_bytes())


@contextlib.contextmanager
def build_directory(parent, keep):
    if keep:
        directory = tempfile.mkdtemp(prefix="pelican-preview-", dir=parent)
        print(f"preview_pelican: retaining build directory: {directory}", file=sys.stderr)
        yield directory
    else:
        with tempfile.TemporaryDirectory(prefix="pelican-preview-", dir=parent) as directory:
            yield directory


def parser():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("input", nargs="?", default="-", help="input file, or - for stdin (default)")
    p.add_argument("-o", "--output", default="-", help="HTML destination; default: stdout")
    p.add_argument("-s", "--settings", type=Path, default=ROOT / "articles/publishconf.py")
    runtime = p.add_mutually_exclusive_group()
    runtime.add_argument("--python", help="Python executable containing Pelican")
    runtime.add_argument("--venv", type=Path, help="virtual environment containing Pelican")
    p.add_argument("--cwd", type=Path, help="build working directory (default: settings directory)")
    p.add_argument("--content-root", type=Path, help="override configured PATH")
    p.add_argument("--source-path", help="logical path relative to content root, including extension; stdin default: preview.md")
    p.add_argument("--kind", choices=["auto", "article", "page"], default="auto")
    p.add_argument("--full-context", action="store_true", help="process all configured content for cross-post dependencies")
    p.add_argument("--rendered-path", help="explicit generated path relative to temporary output, for custom plugins")
    p.add_argument("--set", action="append", default=[], metavar="KEY=JSON", help="override a Pelican setting; repeatable")
    p.add_argument("--temp-dir", type=Path, help="parent for temporary build directory")
    p.add_argument("--timeout", type=float, default=60, help="build timeout in seconds (default: 60)")
    p.add_argument("--debug", action="store_true", help="show build command, Pelican debug logs and error tracebacks on stderr")
    p.add_argument("--keep-build", action="store_true", help="retain temporary sources, outputs and job file for inspection, even on failure")
    return p


def main():
    p = parser()
    args = p.parse_args()
    try:
        settings = args.settings.resolve(strict=True)
        cwd = (args.cwd or settings.parent).resolve(strict=True)
        source = Path(args.input).resolve(strict=True) if args.input != "-" else None
        destination = Path(args.output).absolute() if args.output != "-" else None
        if destination and destination.resolve() in {source, settings, Path(__file__).resolve()}:
            raise ValueError("output must not overwrite the input, settings, or tool")
        if args.timeout <= 0:
            raise ValueError("--timeout must be positive")
        for value in [args.source_path, args.rendered_path]:
            if value:
                relative_path(value)
        overrides = {}
        for item in args.set:
            key, separator, value = item.partition("=")
            if not separator or not key.isupper():
                raise ValueError("--set requires an uppercase KEY=JSON")
            if key in ISOLATED:
                raise ValueError(f"{key} is managed by the tool for build isolation")
            overrides[key] = json.loads(value)
        if args.content_root:
            overrides["PATH"] = str(args.content_root.resolve(strict=True))
        if args.python:
            python = shutil.which(args.python)
            if not python:
                raise ValueError(f"Python executable not found: {args.python}")
            python = os.path.abspath(python)
        elif args.venv:
            python = str(args.venv.absolute() / "bin/python")
        else:
            candidates = [settings.parent / ".venv/bin/python", settings.parent.parent / ".venv/bin/python"]
            python = next((str(path) for path in candidates if path.is_file()), sys.executable)
        with build_directory(args.temp_dir, args.keep_build) as directory:
            work = Path(directory).resolve()
            if source is None:
                (work / "stdin").write_bytes(sys.stdin.buffer.read())
            job = dict(work=str(work), settings=str(settings), input=str(source) if source else None,
                       overrides=overrides, source_path=args.source_path, kind=args.kind,
                       full_context=args.full_context, rendered_path=args.rendered_path, debug=args.debug)
            job_path = work / "job.json"
            job_path.write_text(json.dumps(job))
            command = [python, str(Path(__file__).resolve()), "--_worker", str(job_path)]
            if args.debug:
                print(f"preview_pelican: cwd: {cwd}", file=sys.stderr)
                print(f"preview_pelican: command: {shlex.join(command)}", file=sys.stderr)
                print(f"preview_pelican: settings: {settings}", file=sys.stderr)
            subprocess.run(command, cwd=cwd, stdout=sys.stderr, check=True, timeout=args.timeout)
            data = (work / "result").read_bytes()
            if destination:
                # Replace only after successful rendering; never expose partial HTML.
                name = None
                try:
                    with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as stream:
                        name = stream.name
                        stream.write(data)
                    os.replace(name, destination)
                finally:
                    if name and os.path.exists(name):
                        os.unlink(name)
            else:
                sys.stdout.buffer.write(data)
        return 0
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        if args.debug:
            traceback.print_exc(file=sys.stderr)
        print(f"preview_pelican: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--_worker":
        try:
            worker(sys.argv[2])
        except Exception as error:
            try:
                debug = json.loads(Path(sys.argv[2]).read_text()).get("debug", False)
            except (OSError, ValueError):
                debug = False
            if debug:
                traceback.print_exc(file=sys.stderr)
            print(f"preview_pelican: build failed: {error}", file=sys.stderr)
            sys.exit(1)
    else:
        sys.exit(main())
