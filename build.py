#!/usr/bin/env python3
## INFO ########################################################################
##                                                                            ##
##                          Rust Syntax Highlighter                           ##
##                          =======================                           ##
##                                                                            ##
##                       Version: 0.1.00.071 (20141110)                       ##
##                               File: build.py                               ##
##                                                                            ##
##            For more information about the project, please visit            ##
##                    <https://github.com/petervaro/rust>.                    ##
##                       Copyright (C) 2014 Peter Varo                        ##
##                                                                            ##
##  This program is free software: you can redistribute it and/or modify it   ##
##   under the terms of the GNU General Public License as published by the    ##
##       Free Software Foundation, either version 3 of the License, or        ##
##                    (at your option) any later version.                     ##
##                                                                            ##
##    This program is distributed in the hope that it will be useful, but     ##
##         WITHOUT ANY WARRANTY; without even the implied warranty of         ##
##            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.            ##
##            See the GNU General Public License for more details.            ##
##                                                                            ##
##     You should have received a copy of the GNU General Public License      ##
##     along with this program, most likely a file in the root directory,     ##
##        called 'LICENSE'. If not, see <http://www.gnu.org/licenses>.        ##
##                                                                            ##
######################################################################## INFO ##

# Import python modules
from os.path import join

# Module level constants
CURRENT_DIR = '.'
LANG_PATH  = join(CURRENT_DIR, 'lang')

# Import cutils modules
try:
    import cutils.ccom
    import cutils.clic
    import cutils.cver

    # Update version
    cutils.cver.version(CURRENT_DIR, sub_max=9, rev_max=99, build_max=999)
    # Collect all special comments
    cutils.ccom.collect(CURRENT_DIR)
    # Update header comments
    cutils.clic.header(CURRENT_DIR)
except ImportError:
    print('[WARNING] cutils modules are missing: '
          'install it from http://www.cutils.org')

# Import tmtools modules
try:
    from tmtools.convert import Language
except ImportError:
    from sys import exit
    print('[ ERROR ] tmtools modules are missing: '
          'install it from http://github.com/petervaro/tmtools')
    exit(-1)

#------------------------------------------------------------------------------#
# Import user modules
from src.rust import syntax

# I/O Details of languages and themes
details = {'name' : 'Rusty',
           'path' : LANG_PATH,
           'scope': 'rs',
           'comments' : {'lines': '//',
                         'blocks': ('/*', '*/')},
           'buildsys' : {'build': 'cargo build',
                         'run': 'cargo run',
                         'rebuild': 'cargo clean && cargo build',
                         'rebuild_and_run': 'cargo clean && cargo run'},
           'test_name': 'Rusty_TEST',
           'test_path': '~/Library/Application Support/Sublime Text 3/'
                        'Packages/User/Rusty_TEST'}

# NOTE: Old path to theme files => DO NOT SUPPORT IT:
# '~/Library/Application Support/Sublime Text 3/Packages/Color Scheme - Default'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Setup names and locations
lang = Language(**details)
# Convert and save language file
lang.from_dict(syntax)
lang.write()
