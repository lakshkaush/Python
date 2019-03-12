#! /usr/bin/env python 
""" Find if a string is a palindrome """

def is_palindrome(s):
    string_length = len(s)
    i = 0 
    j = string_length - 1
    
    while (i<j):
        if s[i] == s[j]:
            i +=1 
            j -=1
        else:
            #Not a palindrome
            return 0
    #Is a palindrome
    return 1
    
    
    

def main():
    string = raw_input("Enter string to test")
    is_palindrome(string)

if "__main__" == __name__:
    main()