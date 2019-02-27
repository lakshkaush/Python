""" A sample program to play roll a dice game """
""" Using random.randint """

import random

# Variables 
sides = 0
min = max = 1
result = 0
again = 'y'

print "Welcome to Roll Dice Game"
sides = input("Enter number of sides of die - ")
print ("%d sided dice" % sides)
max = sides 

# Rolling dice now 

while (again == 'y') or (again == 'yes'):
    result = random.randint(min,max)
    print "Result is : ",result
    again = raw_input("Do you want to play again? ")

print "Exiting game"
# End








 

