#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
"""
qslaunch.helpers.mail
~~~~~~~~~~~~~~~~~~~~~

Provides helper functions for Mail.app.

Execute helpers
-----------------------------------------------------------------------------

.. autofunction:: color

Commands
-----------------------------------------------------------------------------

.. autofunction:: cmd_color


..
    :copyright: 2010 Serge Émond
    :license: Apache License 2.0
"""

from appscript import *

mail_app = u'/Applications/Mail.app'
allowed_colors = [ 'blue', 'gray', 'green', 'none', 'orange', 'purple', 'red', 'yellow']
# and "other" ??

#############################################################################
################################################################# shortcuts #
#############################################################################

def color_selected_msgs(color='none'):
    """
    :func:`qslaunch.execute` helper for :func:`cmd_color_selected_msgs`.
    
    See :func:`cmd_color_selected_msgs` for usage.
    
    """
    return (cmd_color_selected_msgs, (), {'color': color})


#############################################################################
################################################################## commands #
#############################################################################


def cmd_color_selected_msgs(color):
    """
    Change the background color of the selected messages in Mail.app.
    
    :param color:
        color name. The list is restricted to:
        'blue', 'gray', 'green', 'none', 'orange', 'purple', 'red', 'yellow'
    
    Example::
    
        ...
        (r'^colormail-(?P<color>.*)$', mail.color_selected_msgs()),
        ...
    
    """
    if color not in allowed_colors:
        raise Exception("Unsupported color '%s'" % color)
    
    mail = app(mail_app)
    msgs = mail.selection.get()
    if len(msgs) < 1:
        raise Exception("Please select messages in Mail.app")
    
    [msg.background_color.set(getattr(k, color)) for msg in msgs]
