#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

#This program is different because it contains if else statements.
#Lines 11-14 make it so that different things will happen based on the input.
# Lines 12 and 14 are indented because they are part of the blocks under if and else. 
print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red'):
    print('Correct!')
else:
    print('Sorry, try again.')
#If Red is not capitalized, it is treated as wrong.
#This tell us that variables, like color, are case-sensitive.