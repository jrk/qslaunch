#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
"""
qslaunch.utils.sysevents
------------------------

..
    :copyright: 2010 Serge Émond
    :license: Apache License 2.0
"""

from appscript import *

def click_menu(process_name, menu_bar_id, *args):
    """Short cut to click a manu through System Events.
    
    :param process_name: ex: u'TextMate'
    :param menu_bar_id: probably always 1
    :param args: the menus to click
    
    Exemples::
    
        click_menu('TextMate', 1, 'File', 'New From Template', 'Python', 'Python Script')
        click_menu('TextMate', 1, 'File', u'Open\u2026')
    
    .. note::
    
        (\u2026 is the "..." char)
    
    .. note::
    
        this ONLY works if the process has been activated first!
        E.g. app(u'TextMate').activate()
    
    """
    se = app(u'/System/Library/CoreServices/System Events.app')
    ap = se.application_processes[process_name]
    mb = ap.menu_bars[menu_bar_id]
    item_names = list(args)
    last_item_name = item_names.pop(0)
    item = mb.menu_bar_items[last_item_name]
    
    for item_name in item_names:
        item = item.menus[last_item_name].menu_items[item_name]
        last_item_name = item_name
    
    item.click()

