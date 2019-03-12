#! /usr/bin/env python
""" Sample code to find the longest palindrome substring """
from palindrome import is_palindrome
import collections

def longest_palindrome_substr(s):
    out_s = s[0]
    count = 0
    max_count = 0
    str_len = len(s)
    j = str_len - 1
    #print "string length", j 
    dict = collections.defaultdict(list)
    #print "dict is", dict
    
    for i in range (0,j):
        out_s = s[i]
        #print "i is", i
        for n in range(i+1,j+1):
            #print " \n \n n is", n
            if s[i] == s[n]:
                out_s += s[n]
                result = is_palindrome(out_s)
                if result:
                    max_count = len(out_s) 
                    dict[max_count].append(out_s)
                else:
                    max_count = 0         
                       
            else:
                max_count = 0
                out_s += s[n]

    print " Palindrome Dict is now", dict
    if not dict:
        print "empty dict.. No palindrome found in string", s
        return 0
    else:
        out_key,output = find_longest_palindrome(dict)
        print "FINAL ANSWER IS...... substring(s) {0} with length {1}".format(output, out_key)
    return 1
 

def find_longest_palindrome(dict):
    max_value = 0
    max_key = max(dict,key=int)          
    return (max_key,dict[max_key])
                                  
                
    
def main():
    string = raw_input("Enter input string: ")
    longest_palindrome_substr(string)

if "__main__" == __name__:
    main()
        