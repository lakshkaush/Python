#! /usr/bin/env python

"""
Trying out option parser. Writing a wrapper around existing option parser wrapper 
"""

from optparse import OptionParser

# Option parse object
parser = OptionParser()

class OptParser:
    """ Option parser wrapper """
    """ This class is intended to provide more flexibility to the Python OptionParse"""

    # Class Data
    usage = "Option parser"
    input_arg = None
    filename = "out.txt"

    def __init__(self):
        """ Constructor """
        print "In class __init___"
    
    def take_one_argument(self,argument):
        """ Function for parser to take one argument"""
        self.input_arg = argument
        parser.add_option("-i","--input", dest = self.input_arg, help= "Take an argument")
        (options, args) = parser.parse_args()
        return (options, args)


def main():
    
    # Class Instance
    O = OptParser()
    (opt,args) = O.take_one_argument('version')
    print opt
    print args



if "__main__" == __name__:
    main()
