===========================
Pelican - category template
===========================

.. image:: https://travis-ci.org/hrbonz/pelican-category_template.png?branch=master
   :target: https://travis-ci.org/hrbonz/pelican-category_template

.. image:: http://img.shields.io/badge/license-BSD%203--Clause-blue.svg
    :target: http://opensource.org/licenses/BSD-3-Clause
    :alt: license BSD 3-Clause

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

License
-------

pelican-category_template is published under a BSD 3-clause license, see the
LICENSE file distributed with the project.
