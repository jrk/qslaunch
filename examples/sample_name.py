#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
"""
sample_name.py
~~~~~~~~~~~~~~

:copyright: 2010 Serge Émond
:license: Apache License 2.0

Sample qslaunch script based on the *program name*.

Setup
-----

For example, lets assume you have a directory `~/quicksilver_commands`
and this script exists as `~/qs_iterm_launcher.py` and id executable.

cd-ing to `~/quicksilver_commands` and typing:

.. code-block:: console

    ln ~/qs_iterm_launcher.py something

will create a hardlink to this script. The "program name", when
executed, will be "something".

Lets also assume you have registered `~/quicksilver_commands` in
Quicksilver's custom catalog...

Bringing Quicksilver's window and typing "something" should find
the "something" in "~/quicksilver_commands".

Executing the "Run" action on this will execute the script with
"something" as the program name.

.. note::

    files ending with ".com" and ".net" don't seem to get executed.
    
    Simply adding ".py" will correct the problem.


Rule explanation
----------------

If "something" is "local", this will open up a new iTerm *tab*
based on the bookmark named "A Local Shell". If that bookmark
doesn't actually exist in iTerm, iTerm will use the *default*
bookmark.

If "something" is "local-finder", this will also cd to the
front most Finder window's path.

If "something" is "gnuplot", it'll open a new *window*, then
start "gnuplot" in it (assuming it's installed on your system).

If "something" is "s-myserver", it'll open a new *tab* and start
an ssh session to "myserver.example.org".

If "something" is "sdfdf", it'll pop an error using growl,
if growl's python bindings are installed.

"""

import sys
import os

from qslaunch import execute
from qslaunch.helpers import iterm
from qslaunch.utils import finder

commands = [
    # Local
    (r'^local$', iterm.bookmark('A Local Shell', 'tab')),
    (r'^local-finder$', iterm.bookmark('A Local Shell', 'tab', cd=finder.front_most_path)),
    
    # ssh to "XX.example.org."
    (r'^s-(?P<server>[^\.]*)$', iterm.shell_exec('ssh %(server)s.example.org.', 'tab')),
    # ssh to full server name with '.' added
    (r'^s-(?P<server>.*)$', iterm.shell_exec('ssh %(server)s.', 'tab')),
    
    # Stuff
    (r'^gnuplot$', iterm.shell_exec('/bin/bash -l -c gnuplot'))
]

def main():
    # Strip path
    command = os.path.basename(sys.argv[0])
    if command[-3:] == '.py':
        # Strip '.py' extension
        command = command[0:len(command)-3]
    execute(command, commands)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        from qslaunch.utils.growl import growl_error
        growl_error("QS Launch Helper", e.args[0])
        raise

