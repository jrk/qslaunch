#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
"""
setup.py

:copyright: 2010 Serge Émond
:license: Apache License 2.0
"""

__version__ = '0.3.0'

from setuptools import setup, find_packages

setup(
    name='qslaunch',
    version= __version__,
    description='Simple QuickSilver launcher helper',
    long_description=u"""\
``qslaunch`` is a small framework to facilitate launching shell stuff from Quicksilver_.

The latest version is available in a `Mercurial repository`_.

.. _Mercurial repository: http://bitbucket.org/greyw/qslaunch/
.. _Quicksilver: http://www.blacktree.com/
""",
    author=u'Serge Émond',
    author_email='greyl@greyworld.net',
    url='http://greyworld.net/en/projects/qslaunch/',
    license='Apache License 2.0',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    install_requires=["appscript"],
    packages=find_packages(),
    zip_safe=False,
    )
