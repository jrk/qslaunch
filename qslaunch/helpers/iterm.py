#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
"""
qslaunch.helpers.iterm
~~~~~~~~~~~~~~~~~~~~~~

Provides helper functions for opening iTerm sessions.

Execute helpers
-----------------------------------------------------------------------------

.. autofunction:: bookmark
.. autofunction:: shell_exec

Commands
-----------------------------------------------------------------------------

.. autofunction:: cmd_bookmark
.. autofunction:: cmd_exec

iTerm helpers
-----------------------------------------------------------------------------

.. autofunction:: current_terminal_window
.. autofunction:: new_terminal_window

..
    :copyright: 2010 Serge Émond
    :license: Apache License 2.0
"""

from appscript import *

iterm_app_name = u'/Applications/iTerm.app'

#############################################################################
################################################################# shortcuts #
#############################################################################

def bookmark(name, where='window', cd=None):
    """
    :func:`itermlaunch.execute` helper for :func:`cmd_bookmark`.
    
    See :func:`cmd_bookmark` for usage.
    
    """
    return (cmd_bookmark, (), {'bookmark': name, 'where': where, 'cd': cd})

def shell_exec(command, where='window', title=None):
    """
    :func:`itermlaunch.execute` helper for :func:`cmd_exec`.
    
    See :func:`cmd_shell_exec` for usage.
    
    """
    return (cmd_exec, (), {'command': command, 'title': title})

#############################################################################
################################################################## commands #
#############################################################################


def cmd_bookmark(bookmark, where='window', cd=None):
    """
    Create a new iTerm session in a new window or tab and launch the
    specified session in it.
    
    :param bookmark: bookmark name. It doesn't exist, iTerm uses the default bookmark
    :param where: string: either 'window' or 'tab'
    :param cd: string or callable
    
    If ``where='tab'`` and there are no windows, a new one is created.
    
    If the ``cd`` parameter is a callable, the return value must be
    a string.
    
    """
    
    if callable(cd):
        cd_path = cd()
        if not isinstance(cd_path, basestring):
            raise Exception("Error obtaining path from %r" % cd)
        cd = cd_path
        del(cd_path)
    
    if where == 'tab':
        term = current_terminal_window()
    else:
        term = new_terminal_window()
    term.launch_(session=bookmark)
    
    if isinstance(cd, basestring):
        sess = term.current_session()
        sess.write(text=u"cd '%s'" % cd.replace("'", "'\\''"))
    

def cmd_exec(command, **kwargs):
    """
    Create a new iTerm session in a new window or tab and execute the
    specified shell commande inside.
    
    :param command: shell command to execute
    :param where: where to open the session ('window' or 'tab', default = 'window')
    :param title: title to gove to the terminal
    
    """
    if 'where' in kwargs and kwargs['where'] == 'tab':
        term = current_terminal_window()
    else:
        term = new_terminal_window()
    s = term.make(new=k.session)
    if 'title' in kwargs and kwargs['title'] is not None:
        s.name.set(kwargs['title'])
    if len(kwargs) > 0:
        command = command % kwargs
    s.exec_(command=command % kwargs)


#############################################################################
################################################################### helpers #
#############################################################################

def current_terminal_window():
    """
    Return the front most iTerm "terminal".
    
    If there are no windows, create a new one.
    
    """
    iterm = app(iterm_app_name)
    iterm.launch()
    iterm.activate()
    term = iterm.current_terminal()
    if term is None:
        term = iterm.make(new=k.terminal)
    return term

def new_terminal_window():
    """
    Return a new, empty iTerm "terminal".
    
    """
    iterm = app(iterm_app_name)
    iterm.launch()
    iterm.activate()
    return iterm.make(new=k.terminal)

