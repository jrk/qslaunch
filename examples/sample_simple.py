#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
"""
sample_simple.py
~~~~~~~~~~~~~~~~

:copyright: 2010 Serge Émond
:license: Apache License 2.0

Simple example.

This script can only do one thing: start a new iTerm window with
a local shell in it, based on the profile "A Local Shell".

If the profile doesn't exist, iTerm will use the default profile.

To use from Quicksilver, simply copy in a directory registered in its
catalog, and refresh the catalog (or restart QS).

Make sure the script is executable!

"""

from qslaunch.helpers import iterm

if __name__ == '__main__':
    iterm.cmd_bookmark('A Local Shell')

