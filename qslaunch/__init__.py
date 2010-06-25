#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
"""
qslaunch
~~~~~~~~

..
    :copyright: 2010 Serge Émond
    :license: Apache License 2.0

"""

VERSION = (0, 3, 1, 'final', 0)

def get_version(full=False):
    """Return version number."""
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3:] == ('alpha', 0):
        version = '%s pre-alpha' % version
    elif VERSION[3] != 'final' or full:
        version = '%s %s %s' % (version, VERSION[3], VERSION[4])
    # from .utils.version import get_hg_revision
    # hg_rev = get_hg_revision()
    # if hg_rev != u'HG-unknown':
    #     version = "%s %s" % (version, hg_rev)
    return version


import re

class NoSuchCommand(Exception):
    """Exception raised when command could not be found."""
    pass

def execute(name, patterns):
    """Execute a command by finding it in a list of patterns.
    
    :param name: name to lookup in the pattern list
    :param patterns: list of patterns
    
    The list of patterns is a list of tuples, referenced here as "pattern".
    
    A "pattern" tuple has two items:
    
    1. regular expression to match
    2. command
    
    The command is also a tuple, with three elements:
    
    1. the function to call
    2. positional arguments (tuple)
    3. named arguments (dict)
    
    If the patterns contains named references (e.g. (?P<xx>yyy)), these will
    be also placed in the named arguments dictionary.
    
    Example::
    
        patterns = [
            (r'^x-(?P<tag>.*)$', (somefunc, (), {a=17})),
        ]
        execute('x-abc', patterns)
    
    Will call ``somefunc(a=17, tag='abc')``.
    
    """
    for pat in patterns:
        m = re.search(pat[0], name)
        if m is not None:
            cmd = pat[1][0]
            args = pat[1][1]
            kwargs = pat[1][2]
            kwargs.update(m.groupdict())
            return cmd(*args, **kwargs)
    raise NoSuchCommand(u"Can’t find command: %s" % name)

