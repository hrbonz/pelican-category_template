===========================
Pelican - category template
===========================

.. image:: https://travis-ci.org/hrbonz/pelican-category_template.png?branch=master
   :target: https://travis-ci.org/hrbonz/pelican-category_template

Load a template for any content (article, page) based on its category.  For
example, for an article, if a template named ``article-<category>.html`` exists
in the theme or Jinja2 path, it will be used. If not, then the default template
is used.


Install
-------

Use pip to install the plugin:

.. code:: sh

    $ pip install pelican-category_template


Usage
-----

To use the plugin, add it to the ``PLUGINS`` list in your configuration file.
Put it in ``pelicanconf.py`` by default:

.. code:: python

    PLUGINS = [
        # ...
        'categorytpl'',
    ]


Test
----

.. code:: sh

    $ python -m unittest discover
