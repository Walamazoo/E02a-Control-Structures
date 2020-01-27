#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

#I expect line 9 to take the input and make all letters lowercase.
#This is to solve the problem of capital letters being present.
print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')
#If a space is added before or after, it is treated as wrong.
#This tells us that spaces are counted as characters. 