#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
"""
qslaunch.utils.growl
--------------------

..
    :copyright: 2010 Serge Émond
    :license: Apache License 2.0

"""

def growl_error(error_title, error_body):
    """
    Output an error message through Growl.
    
    :param error_title: Growl title
    :param error_body: Message body
    
    The application is registered in Growl as "qslaunch.py".
    
    If Growl cannot be imported, nothing happens.
    
    """
    try:
        import Growl
        gn = Growl.GrowlNotifier(applicationName='qslaunch.py', notifications=['error'])
        gn.register()
        gn.notify('error', error_title, error_body)
    except:
        pass
