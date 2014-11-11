Rust language bundles
=====================

This repo is about Rust related bundles for Sublime Text 3 and TextMate
editors and for online usage.

Rust
----

Rust Rocks!


Installation
------------

***Via Package Control***

The fastest and easiest way to install these packages for Sublime Text is the
following:

1. Install [Package Control](https://sublime.wbond.net/installation)
2. Open `Tools` → `Command Palette`
3. Select `Package Control: Install Package`
4. Search for `Rust`
5. Happy coding ;)

***Set as default***

After you installed the language definition file successfully, all you have to
do is assign the `.py` files to always open with this syntax highlighter. Go to

`View` → `Syntax` → `Open all with current extension as...` → `Rust`

To remove this setting, you can always overwrite this preference.

***Manual installation***

Download the `tmLanguage` files from the python and Cython branches of this
repository. Navigate to your `Packages` folder and create a `Python3` and/or a
`Cython` folder(s) and copy the `tmLanguage` and sublime-build files into.


Contribute
----------

Any help is appreciated and more than welcome -- my goal is to make this the
*'de facto'* language bundle for python 3. If you want to submit a change,
please use the following conventions when editing the original python files:

- variables uses `underscore_separated_names`;
- all files uses 4 spaces for indentation;
- `=` and `:` operators are aligned if length of variable names are similar;
- `(`, `[` and `{` start a new line, if possible and reasonable;
- each line must fit in the width 80 columns (code, text, etc.);
- comment separators can be easily generated with the `src.utils.separator()`
function


LICENSE
-------

Copyright (C) 2014 Peter Varo

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program, most likely a file in the root directory, called 'LICENSE'. If
not, see http://www.gnu.org/licenses.
