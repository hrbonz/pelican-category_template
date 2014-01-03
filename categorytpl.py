# -*- coding: utf-8 -*-
"""A `pelican <https://github.com/getpelican/pelican>`_ plugin to apply
a template based on the category of the content.

Taking the default template name for this content, suffix it with a dash
character ('-') and the category name. If this template exists, use it
instead of the standard one. This way pages can be customized based on
different categories.

For example, 'article-misc.html' could be used as template for an
article with a category 'misc'.
"""

from pelican import signals

__author__ = "Stefan \"hr\" Berder"
__contact__ = "hr@bonz.org"
__license__ = "BSD 2-Clause"
__version__ = "v0.0.2"

SEP = '-'

def category_template(generator, content):
    """Get a generator and a content, try to load a template based on
    the category of the document.

    :param generator: a pelican generator instance
    :type generator: ``pelican.generator.Generator``
    :param content: a pelican content instance
    :type content: ``pelican.content.Content``
    """
    if hasattr(content, 'category') and content.category:
        categorytpl = u"{}{}{}".format(content.template, SEP,
                                       content.category)
        try:
            generator.get_template(categorytpl)
        # if the template is not found, keep the original one
        except Exception:
            return
        content.template = categorytpl

def register():
    signals.article_generator_write_article.connect(category_template)
