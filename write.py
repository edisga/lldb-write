import lldb

def __lldb_init_module (debugger, dict):
  debugger.HandleCommand('command script add -f write.write_to_file write')

def write_to_file(debugger, filename, command, result, dict):
  f=open(filename,'w')
  debugger.SetOutputFileHandle(f,True)
  debugger.HandleCommand(command,result)  
  f.close()
  debugger.SetOutputFileHandle(sys.__stdout__, True)

