from __future__ import print_function
import lldb
#import argparse


#def parse_args(raw_args):
    #"""Parse the arguments given to write"""
    # Need to provide 'prog' (name of program) here otherwise
    # argparse tries to get it from sys.argv[0], which breaks
    # when called in lldb.
    #parser = argparse.ArgumentParser(
    #    prog='write',
    #    description='Write the output of an lldb command to file'
    #)

    #parser.add_argument('filename')
    #parser.add_argument('command', nargs='+')

    #args = parser.parse_args(raw_args.split(' '))

    # The parser splits the command into a list of strings e.g.
    # ['register', 'read']
    # we convert it back to a string so we can later pass it to
    # lldb for evaluation
    #args.command = ' '.join(args.command)

    #return args

def write_to_file(filename, command, output):
    """Write the output to the given file, headed by the command"""
    #with open(filename, 'w') as f:
        #f.write("(lldb) " + command + '\n\n')
        #output.PutOutput(f);
        #output.flush();
        #f.flush();
    f = open(filename, 'w');
    output.PutOutput(f);
    output.flush();
    f.flush();
    f.close();

def handle_call(debugger, raw_args, result, internal_dict):
    """Receives and handles the call to write from lldb"""
    #args = parse_args(raw_args)
    show_output = True;
    args = raw_args.split();
    
    filename = args.pop(0);
    if args[0] == '-h':
        show_output = False;
        args.pop(0);
    command = ' '.join(args);
    
    print('Args: ' + ' '.join(args));
    print('filename: ' + filename);
    print('command: ' + command);
    # Run the command and store the result
    res = lldb.SBCommandReturnObject()
    with open(filename, 'w') as f:
        res.SetImmediateOutputFile(f);
        interpreter = lldb.debugger.GetCommandInterpreter()
        interpreter.HandleCommand(command, res)

    # Get the output even
    
    if not (res.Succeeded()):
        print(res.GetError(), end='');
        return;
    
    if show_output:
        output = res.GetOutput()
        print(output, end='');
    
    #write_to_file(filename, command, res)

def __lldb_init_module(debugger, internal_dict):
    """Initialise the write command within lldb"""
    # Tell lldb to import this script and alias it as 'write'.
    # > Note: 'write' (from 'write.handle_call') is taken from the
    #   name of this file
    debugger.HandleCommand('command script add -f write.handle_call write')

    print('The "write" command has been loaded and is ready for use.')

