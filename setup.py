#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8 -*-
"""
setup.py

:copyright: 2010 Serge Émond
:license: Apache License 2.0
"""

from distutils.core import setup
from distutils.command.install_data import install_data
from distutils.command.install import INSTALL_SCHEMES
import os
import sys

class osx_install_data(install_data):
    # On MacOS, the platform-specific lib dir is /System/Library/Framework/Python/.../
    # which is wrong. Python 2.5 supplied with MacOS 10.5 has an Apple-specific fix
    # for this in distutils.command.install_data#306. It fixes install_lib but not
    # install_data, which is why we roll our own install_data class.
    
    def finalize_options(self):
        # By the time finalize_options is called, install.install_lib is set to the
        # fixed directory, so we set the installdir to install_lib. The
        # install_data class uses ('install_data', 'install_dir') instead.
        self.set_undefined_options('install', ('install_lib', 'install_dir'))
        install_data.finalize_options(self)



if sys.platform == "darwin":
    cmdclasses = {'install_data': osx_install_data}
else:
    cmdclasses = {'install_data': install_data}

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

# Tell distutils to put the data_files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

packages, data_files = [], []
walk_paths = ['qslaunch']
for walk_path in walk_paths:
    for dirpath, dirnames, filenames in os.walk(walk_path):
        # Ignore dirnames that start with '.'
        for i, dirname in enumerate(dirnames):
            if dirname.startswith('.'): del dirnames[i]
        if '__init__.py' in filenames:
            packages.append('.'.join(fullsplit(dirpath)))
        elif filenames:
            data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

scripts = []
for dirpath, dirnames, filenames in os.walk('bin'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    scripts += [os.path.join(dirpath, f) for f in filenames]


# Dynamically calculate the version based on agifm.VERSION.
version = __import__('qslaunch').get_version()
if u'HG' in version:
    version = ' '.join(version.split(' ')[:-1])

setup(name='qslaunch',
    version= version.replace(' ', '-'),
    description='Simple QuickSilver launcher helper',
    author='Serge Emond',
    author_email='greyl@greyworld.net',
    license='Apache License 2.0',
    url='http://greyworld.net/en/projects/qslaunch/',
    packages=packages,
    cmdclass=cmdclasses,
    data_files=data_files,
    scripts=scripts,
    install_requires=["appscript"],
    )
