#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
"""
setup.py

:copyright: 2010 Serge Émond
:license: Apache License 2.0
"""

from setuptools import setup, find_packages
from qslaunch import get_version

setup(
    name='qslaunch',
    version= get_version().replace(' ', '-'),
    description='Simple QuickSilver launcher helper',
    long_description=u"""\
``qslaunch`` is a small framework to facilitate launching shell stuff from Quicksilver.

See also:
- `Mercurial repository`_
- `Documentation`_

.. _Mercurial repository: http://bitbucket.org/greyw/qslaunch/
.. _Documentation: http://packages.python.org/qslaunch/
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
