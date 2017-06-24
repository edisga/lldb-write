# lldb-write
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A Python script for `lldb` that writes the output of a command to a given file.

## Installation

Import the script manually:

`(lldb) command script import /path/to/lldb-write/write.py`

Or add `command script import /path/to/lldb-write/write.py` to ~/.lldbinit.


## Usage

`(lldb) write filename command`

Example:

`(lldb) reg.txt register read`