from __future__ import print_function
import lldb
import os
import lldb

def __lldb_init_module (debugger, dict):
  debugger.HandleCommand('command script add -f write.write_to_file write')

def write_to_file(debugger,command, result, dict):
  f=open(filename, 'w')
  debugger.SetOutputFileHandle(f,True);
  debugger.HandleCommand(command)
  f.close();
  debugger.SetOutputFileHandle(sys.stdout, True)

