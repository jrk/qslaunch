#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
"""
qslaunch.utils.finder
---------------------

..
    :copyright: 2010 Serge Émond
    :license: Apache License 2.0
"""

from appscript import *
from appscript.reference import CommandError

def front_most_path():
    """Return the path of the active finder window, or None."""
    try:
        return app(u'Finder').windows[1].target.get(resulttype=k.alias).path
    except CommandError:
        return None

