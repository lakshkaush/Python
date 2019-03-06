#! /usr/bin/env python
""" Sample python code to test imports from libs """

from py_util import execute_command

def main():
    execute_command("ls")

if "__main__" == __name__:
    print "In main program"
    main()
    