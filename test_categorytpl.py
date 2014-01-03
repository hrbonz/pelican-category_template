# -*- coding: utf-8 -*-
import os
import unittest

from pelican.contents import Article
from pelican.generators import Generator
from pelican.settings import DEFAULT_CONFIG

from categorytpl import category_template

class TestCategoryTpl(unittest.TestCase):
    def setUp(self):
        settings = DEFAULT_CONFIG.copy()
        settings['EXTRA_TEMPLATES_PATHS'] = ['.']
        context = settings.copy()
        self.generator = Generator(context, settings, settings['PATH'],
                                   settings['THEME'], settings['OUTPUT_PATH'])

    def test_no_category(self):
        content = Article(content=u'', metadata={})
        category_template(self.generator, content)
        self.assertEqual(content.template, 'article')

    def test_category_no_tpl(self):
        content = Article(content=u'', metadata={u'category': u'misc'})
        category_template(self.generator, content)
        self.assertEqual(content.template, 'article')

    def test_category_with_tpl(self):
        content = Article(content=u'', metadata={u'category': u'misc'})
        with open('article-misc.html', 'w') as fd: fd.write('foobar')
        category_template(self.generator, content)
        self.assertEqual(content.template, 'article-misc')
        os.remove('article-misc.html')

if __name__ == '__main__':
    unittest.main()
