# Code imported from https://github.com/4iar/lldb-write

from __future__ import print_function
import lldb
import argparse
import os

import lldb

def parse_args(raw_args):
    """Parse the arguments given to write"""
    # Need to provide 'prog' (name of program) here otherwise
    # argparse tries to get it from sys.argv[0], which breaks
    # when called in lldb.
    parser = argparse.ArgumentParser(
        prog='write',
        description='Write the output of an lldb command to file'
    )

    parser.add_argument('filename')
    parser.add_argument('command', nargs='+')

    args = parser.parse_args(raw_args.split(' '))

    # The parser splits the command into a list of strings e.g.
    # ['register', 'read']
    # we convert it back to a string so we can later pass it to
    # lldb for evaluation
    args.command = ' '.join(args.command)

    return args

def __lldb_init_module (debugger, dict):
  debugger.HandleCommand('command script add -f write.write_to_file write')

def write_to_file(debugger, command, raw_args, result, dict):
  args = parse_args(raw_args)
  f=open(filename, 'w')
  debugger.SetOutputFileHandle(f,True);
  debugger.HandleCommand(command)
  f.close();
  debugger.SetOutputFileHandle(sys.stdout, True)

