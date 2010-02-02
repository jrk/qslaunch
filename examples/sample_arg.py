#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
""""
sample_arg
~~~~~~~~~~

:copyright: 2010 Serge Émond
:license: Apache License 2.0

Sample qslaunch script based on the first argument.

This script could be copied to:

    ``~/Library/Application Support/Quicksilver/Actions``

and be made executable. Then if you restart Quicksilver, you'll have a new
action named "sample_arg".

If you bring up Quicksilver's window and type something, and then
select the action "sample_arg", it'll run this script.

Or you might simply type in a shell:

.. code-block:: console
    
    ./sample_arg.py something

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
    try:
        command = sys.argv[1]
    except IndexError:
        raise Exception("Missing 'command' argument to %s" % sys.argv[0])
    execute(command, commands)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        from qslaunch.utils.growl import growl_error
        growl_error("QS Launch Helper", e.args[0])
        raise

