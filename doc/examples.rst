.. -*- Mode: reStructuredText; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-

Examples
=============================================================================

Simple example
-----------------------------------------------------------------------------

Suppose that you have two bookmarks in iTerm: the first named "local" and the
second named "somewhere".
You could then place two python scripts in a directory and add it to
Quicksilver's catalogue.

The first, named ``local.py``, could contain this::

    #!/usr/bin/env python
    from qslaunch.helpers.iterm import cmd_bookmark
    cmd_bookmark('local')

The second, ``somewhere.py``::

    #!/usr/bin/env python
    from qslaunch.helpers.iterm import cmd_bookmark_in_tab
    cmd_bookmark_in_tab('somewhere')

Typing "local" in Quicksilver would open a new window with a local shell.

Typing "somewhere" would open a new tab in the top window, possibly
with a remote shell defined in iTerm's bookmark manager.

More complex examples
-----------------------------------------------------------------------------

You can find other examples in the "examples" directory of the source.

You can browse this online on `qslaunch's mercurial repository <http://greyworld.net/qslaunch/hg/>`_.

