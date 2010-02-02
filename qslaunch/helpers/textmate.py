#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
"""
qslaunch.helpers.textmate
~~~~~~~~~~~~~~~~~~~~~~~~~

Provide useful shortcuts for TextMate.

Execute helpers
---------------

.. autofunction:: new_from_template
.. autofunction:: set_theme

Commands
--------

.. autofunction:: cmd_new_from_template
.. autofunction:: cmd_set_theme

..
    :copyright: 2010 Serge Émond
    :license: Apache License 2.0
"""

from appscript import *
from ..utils.sysevents import click_menu

tm_app_name = u'/Applications/TextMate.app'
tm_process_name = u'TextMate'

#############################################################################
################################################################# shortcuts #
#############################################################################

def new_from_template(*args):
    """
    Create a new TextMate window based on a specific template.
    
    :param args:
        The path to the template in the "File" menu.
        For example, ``new_from_template('Python', 'Python Script')``
    
    """
    
    return (cmd_new_from_template, (), {'template_path': args})

def set_theme(theme=None):
    """
    Change TextMate's theme.
    
    :param theme: Theme or None
    
    .. note::
    
        If "theme" is None, be sure to define a "theme" backreference in the ereg!
    
    """
    return (cmd_set_theme, (), {'theme': theme})

#############################################################################
################################################################## commands #
#############################################################################


def cmd_new_from_template(template_path):
    """
    Create a new TextMate window from a template.
    
    :param template_path: tuple/list representing the template.
    
    The tuple is the menu items under "New From Template".
    
    Example::
    
        cmd_new_from_template(('Python', 'Python Script'))
    
    """
    app(tm_app_name).activate()
    menus = ['File', 'New From Template'] + list(template_path)
    click_menu(tm_process_name, 1, *menus)


def cmd_set_theme(theme):
    """
    Set the current theme using System Events.
    
    :param theme: Name of the theme
    
    """
    app(tm_app_name).activate()
    se = app(u'System Events')
    se.keystroke(u',', using=[k.command_down])
    setm = se.processes[u'TextMate']
    
    setm.windows[1].tool_bars[1].buttons[u'Fonts & Colors'].click()
    setm.windows[1].pop_up_buttons[1].click()
    setm.keystroke(theme)
    setm.keystroke(u'\r')
    setm.keystroke(u'w', using=[k.command_down])

