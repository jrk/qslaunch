.. -*- Mode: reStructuredText; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-

Installation
=============================================================================

Requirements
-----------------------------------------------------------------------------

This package depends on two other python packages:

* `appscript <http://appscript.sourceforge.net/>`_;
* `Growl’s python bindings <http://growl.info/documentation/developer/python-support.php>`_ (optional).

Growl is not required. It’s only used to pop an error message when a requested command cannot be found.

Installing
-----------------------------------------------------------------------------

To install Growl’s binding, follow the instructions on their page. (The bindings are in Growl’s SDK disk image, not the installation image! You can find it on `Growl’s sources page <http://growl.info/source.php>`_).

To install qslaunch, simply open a terminal and type:

.. code-block:: console

  $ sudo easy_install qslaunch

If appscript is not installed, it should be handled automatically by ``easy_install``.

If using `pip <http://pip.openplans.org/>`_, you can install it directly from the mercurial repository:

.. code-block:: console

  $ sudo pip install hg+http://bitbucket.org/greyw/qslaunch/
