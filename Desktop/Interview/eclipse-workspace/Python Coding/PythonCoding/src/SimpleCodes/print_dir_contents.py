#! /usr/bin/env python
""" Sample code to test recursion.
Recursively looks at dirs and prints out dir contents"""
""" Source - https://www.codementor.io/sheena/essential-python-interview-questions-du107ozr6 """


# Function takes in path name and lists contents in the path

import os

def print_dir_contents(sPath):
    for sChild in os.listdir(sPath):
        # Get full path of the child
        sChildPath = os.path.join(sPath,sChild)
        
        #If child is actually a dir, call func recurrsively
        if os.path.isdir(sChild):
            print_dir_contents(sChild)
        else:
            # This is a file, so print the full path of the file
            print (sChildPath)
        


def main():
    print "In main"
    print "Current dir is {}".format(os.curdir)
    print_dir_contents(os.curdir)
    
if "__main__" == __name__:
    main()