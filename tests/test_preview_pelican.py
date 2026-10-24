"""Integration tests: run with articles/.venv/bin/python -m unittest discover -s tests."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "preview_pelican.py"


class PreviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "content").mkdir()
        (self.root / "theme/templates").mkdir(parents=True)
        for kind in ("article", "page"):
            (self.root / f"theme/templates/{kind}.html").write_text(
                "<!doctype html><title>{{ " + kind + ".title }}</title>{{ " + kind + ".content }}")
        (self.root / "probe.py").write_text('''from pathlib import Path
from pelican import signals

def transform(generator):
    for key in ("articles", "drafts", "pages", "draft_pages"):
        for content in getattr(generator, key, []):
            content._content += "<b>generator-plugin</b>"

def finish(pelican):
    for path in Path(pelican.output_path).rglob("*.html"):
        path.write_text(path.read_text() + "<!-- finalized-plugin -->")
    print("plugin diagnostic")

def register():
    signals.article_generator_finalized.connect(transform)
    signals.page_generator_finalized.connect(transform)
    signals.finalized.connect(finish)
''')
        (self.root / "settings.py").write_text('''PATH = 'content'
THEME = 'theme'
PLUGINS = ['probe']
PLUGIN_PATHS = ['.']
SITEURL = 'https://example.test'
TIMEZONE = 'UTC'
DIRECT_TEMPLATES = []
FEED_ALL_ATOM = CATEGORY_FEED_ATOM = AUTHOR_FEED_ATOM = None
TAG_SAVE_AS = CATEGORY_SAVE_AS = AUTHOR_SAVE_AS = ''
ARTICLE_SAVE_AS = 'nested/{slug}/index.html'
DRAFT_SAVE_AS = 'draft/{slug}.html'
''')
        self.content = b'Title: Test\nDate: 2020-01-01\nCategory: Testing\nSlug: test\n\n**hello**\n'

    def run_preview(self, *args, data=None):
        return subprocess.run([sys.executable, str(TOOL), '--python', sys.executable,
                               '-s', str(self.root / 'settings.py'), *map(str, args)],
                              input=data, capture_output=True)

    def test_file_stdin_parity_and_finalized_plugin(self):
        source = self.root / 'content/test.md'
        source.write_bytes(self.content)
        before = source.stat().st_mtime_ns
        file_result = self.run_preview(source)
        stdin_result = self.run_preview('--source-path', 'test.md', data=self.content)
        self.assertEqual(file_result.returncode, 0, file_result.stderr)
        self.assertEqual(stdin_result.returncode, 0, stdin_result.stderr)
        self.assertEqual(file_result.stdout, stdin_result.stdout)
        self.assertIn(b'<strong>hello</strong>', file_result.stdout)
        self.assertIn(b'generator-plugin', file_result.stdout)
        self.assertTrue(file_result.stdout.endswith(b'<!-- finalized-plugin -->'))
        self.assertNotIn(b'plugin diagnostic', file_result.stdout)
        self.assertIn(b'plugin diagnostic', file_result.stderr)
        self.assertEqual(source.read_bytes(), self.content)
        self.assertEqual(source.stat().st_mtime_ns, before)
        self.assertFalse((self.root / 'output').exists())

    def test_draft_page_and_file_output(self):
        output = self.root / 'preview.html'
        draft = self.content.replace(b'\n\n', b'\nStatus: draft\n\n', 1)
        result = self.run_preview('--kind', 'page', '-o', output, data=draft)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, b'')
        self.assertIn(b'generator-plugin', output.read_bytes())
        self.assertIn(b'finalized-plugin', output.read_bytes())

    def test_failed_build_preserves_destination(self):
        output = self.root / 'preview.html'
        output.write_text('keep me')
        result = self.run_preview('-o', output, data=b'no required metadata')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(output.read_text(), 'keep me')
        self.assertEqual(result.stdout, b'')

    def test_path_traversal_rejected(self):
        result = self.run_preview('--source-path', '../escape.md', data=self.content)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, b'')

    def test_draft_article(self):
        draft = self.content.replace(b'\n\n', b'\nStatus: draft\n\n', 1)
        result = self.run_preview(data=draft)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(b'generator-plugin', result.stdout)

    def test_missing_plugin_fails(self):
        result = self.run_preview('--set', 'PLUGINS=["nonexistent_preview_plugin"]', data=self.content)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, b'')

    def test_debug_and_retained_failed_build(self):
        result = self.run_preview('--debug', '--keep-build', '--temp-dir', self.root,
                                  data=b'missing metadata')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, b'')
        self.assertIn(b'preview_pelican: command:', result.stderr)
        self.assertIn(b'Traceback', result.stderr)
        retained = list(self.root.glob('pelican-preview-*'))
        self.assertEqual(len(retained), 1)
        self.assertTrue((retained[0] / 'job.json').is_file())
        self.assertTrue((retained[0] / 'content/preview.md').is_file())

    def test_debug_keeps_stdout_clean(self):
        result = self.run_preview('--debug', data=self.content)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(result.stdout.startswith(b'<!doctype html>'))
        self.assertNotIn(b'DEBUG', result.stdout)
        self.assertIn(b'DEBUG', result.stderr)

    def test_full_context(self):
        (self.root / 'content/other.md').write_bytes(self.content.replace(b'Test', b'Other').replace(b'test', b'other'))
        result = self.run_preview('--full-context', data=self.content)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(b'<title>Test</title>', result.stdout)


if __name__ == '__main__':
    unittest.main()
