# -*- coding: utf-8 -*-
import os
from setuptools import setup

#import categorytpl

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'pelican-category_template',
    version = "v0.0.2",
    author = "Stefan \"hr\" Berder",
    author_email = "hr@bonz.org",
    license = "BSD 2-Clause",
    py_modules=['categorytpl'],
    url = 'https://github.com/hrbonz/pelican-category_template',
    description='A pelican plugin to apply a template based on the '
    'category of the content.',
    long_description=README,
    install_requires = ['pelican>=3.1.1'],
    classifiers=[
        'Development Status :: 6 - Mature',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet'
    ]
)
