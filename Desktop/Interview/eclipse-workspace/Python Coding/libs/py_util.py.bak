#!/usr/bin/env python

""" 
Main python lib file to get several utilities. 
Intended to be similar to altera.autil usage

"""

__author__= "Lakshitha Kaushik"
__date__ = "$Date: 2019/03/02 $"


# Python Global imports 
import subprocess
import os 

def execute_command(command, **kwargs):
    return subprocess.Popen(command, shell=False, stdin=None, stderr=None, stdout=None)




def get_dir_contents(directory):
    """ Function to get current dir"""
    os.chdir(directory)
    print "The path is now"
    execute_command("ls")
    cmd = "cd"
    return execute_command(cmd)

print "__name__ is", __name__

def main():
    print "In main()"


if "__main__" == __name__:
    print "This is main program so we call the main function"
    main()
else:
    print "Not main program. This program is being imported"
