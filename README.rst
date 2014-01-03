===========================
Pelican - category template
===========================

Load a template for any content (article, page) based on its category.  For
example, for an article, if a template named ``article-<category>.html`` exists
in the theme or Jinja2 path, it will be used. If not, then the default template
is used.


Test
----

.. code-block:: sh

    $ python -m unittest discover
