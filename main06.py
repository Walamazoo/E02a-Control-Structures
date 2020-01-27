#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

#Line 9 is now different because it now also calls the .strip() method
#This will remove spaces at the beginning and end of the input.
print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower().strip() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')
#The logic will still be broken if the user misspells red or otherwise has another character in the input.