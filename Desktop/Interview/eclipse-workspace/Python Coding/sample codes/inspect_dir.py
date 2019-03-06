#! /usr/bin/env python
"""
Program to inspect contents in a given dir. 
Takes in the dir as argument. 

Command - 
    
    python inspect_dir.py -<option> <arg>

----- Available options ---

    -h              : help. Displays help options 
    -i <dir name>   : dir name is the argument. 
                      Displlays details of the specified dir

-----

"""
# Python Global Inputs
import sys
sys.path.insert(0,'./libs')
import py_util
from py_util import execute_command

def main():
    print "Executing command"
    execute_command("ls")

if "__main__" == __name__:
    main()

