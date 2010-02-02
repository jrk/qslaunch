.. -*- Mode: reStructuredText; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-

Overview
=============================================================================

``qslaunch`` is a small framework to launch stuff from `Quicksilver <http://www.blacktree.com/>`_.

The trick is to create a python script containing a bunch of rules.
Quicksilver executes the script using a given *name* that the script
will match against the rules.

If a match is found, the command associated with the rule is executed.

The command can be any python code you supply. Or it can be one of the
included commands…

``qslaunch`` comes with a few predefined commands that can:

* using `iTerm <http://iterm.sourceforge.net/>`_:

  * create an iTerm session (either in a new window or in a new tab of an
    existing window) based on a bookmark as defined in iTerm's bookmark manager;
  * create an iTerm session and execute an arbitrary command in it, allowing
    to start any software requiring the use of a terminal;
  * create an iTerm session in the folder of the current Finder window;
* for `TextMate <http://macromates.com/>`_:

  * change the current theme in TextMate;
  * create a new empty file from a template in TextMate.

The project page is currently hosted on my blog:
`qslaunch <http://greyworld.net/en/projects/qslaunch>`_.

