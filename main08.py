#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

#Line 10 will loop the code in its block until color==red.
#Lines 11-18 are indented because they are in line 10's block.
print('Greetings!')
color = ''
color = input("What is my favorite color? ")
while (color != 'red'):
    color = color.lower().strip()
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')
#With the change, if the input is not red, an infinite loop will occur.