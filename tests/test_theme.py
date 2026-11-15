"""Theme tests: run with articles/.venv/bin/python -m unittest discover -s tests."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
STYLESHEET = ROOT / 'pelican_themes/icecream/static/css/home.css'


def load(name, path):
    spec = spec_from_file_location(name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pelicanconf = load('pelicanconf', ROOT / 'articles/pelicanconf.py')
build_homepage = load('build_homepage', ROOT / 'build_homepage.py')


class MinifyCssTests(unittest.TestCase):
    minify = staticmethod(pelicanconf.minify_css)

    def test_strips_comments_and_whitespace(self):
        self.assertEqual(self.minify('/* x */\na {\n\tcolor: red;\n}\n'),
                         'a{color:red}')

    def test_keeps_descendant_space_before_pseudo_class(self):
        self.assertEqual(self.minify('.a :is(h2, h3) { margin: 0 }'),
                         '.a :is(h2,h3){margin:0}')

    def test_keeps_media_query_and_strings_valid(self):
        self.assertEqual(
            self.minify("@media (width >= 600px) and (x) { li { a: '- ' } }"),
            "@media (width>=600px) and (x){li{a:'- '}}")

    def test_stylesheet_stays_balanced(self):
        css = self.minify(STYLESHEET.read_text())
        self.assertEqual(css.count('{'), css.count('}'))
        self.assertNotIn('/*', css)


class MinifyJsTests(unittest.TestCase):
    def test_drops_comment_lines_and_indentation(self):
        self.assertEqual(
            pelicanconf.minify_js('// a\n\tvar x = 1; // keep\n\n  f();\n'),
            'var x = 1; // keep\nf();')


class RootPagesTests(unittest.TestCase):
    """Homepage and error pages share the blog's head and footer."""

    @classmethod
    def setUpClass(cls):
        env = build_homepage.environment()
        cls.pages = {'index.html': build_homepage.build(env=env)}
        for template, name in build_homepage.ERROR_PAGES.items():
            cls.pages[name] = env.get_template(template).render(
                SITEURL=build_homepage.ERROR_PAGE_SITEURL)

    def test_pages_have_theme_support(self):
        for name, page in self.pages.items():
            with self.subTest(page=name):
                self.assertIn('<meta name="color-scheme" content="light dark">',
                              page)
                self.assertIn('class="theme-switch"', page)
                self.assertRegex(page, r'<style>:root\{[^<]*--paper:')
                self.assertNotRegex(page, r'\{[{%#]')

    def test_urls_are_absolute_on_error_pages(self):
        # Error pages are served at whatever path was requested.
        for name in build_homepage.ERROR_PAGES.values():
            with self.subTest(page=name):
                urls = re.findall(r'(?:src|href)="([^"]+)"|url\(([^)]+)\)',
                                  self.pages[name])
                for url in filter(None, sum(urls, ())):
                    self.assertRegex(url, r'^(/|https?:|mailto:)')

    def test_footer_year_is_current(self):
        year = pelicanconf.CURRENT_YEAR
        for name, page in self.pages.items():
            with self.subTest(page=name):
                self.assertIn(f'2005-{year} Marko Samastur', page)


if __name__ == '__main__':
    unittest.main()
