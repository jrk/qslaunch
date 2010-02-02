#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
"""
qslaunch.utils.version
----------------------

:copyright: 2010 Serge Émond
:license: Apache License 2.0
"""

import qslaunch
import os.path

def get_hg_revision(path=None):
    """
    Get a version from mercurial in the form HG-xx.
    Inspired by Django's get_svn_version()
    
    """
    try:
        from mercurial import ui, hg
    except:
        return u'HG-unknown'
    
    rev = None
    if path is None:
        path = os.path.dirname(os.path.realpath(qslaunch.__path__[0]))
    try:
        repo = hg.repository(ui.ui(), '.')
        head = repo.heads()[0]
        return u'HG-%s' % repo[head].hex()
        # rev = repo[head]._rev
        # return u'HG-%s' % rev
    except:
        pass
    return u'HG-unknown'
