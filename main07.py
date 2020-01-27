#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

#This program is different because it includes an elif.
#Line 13 accounts for a certain input andgives an alternate ouput.
print('Greetings!')
color = input("What is my favorite color? ")
color = color.lower().strip()
if (color == 'red'):
    print('Correct!')
elif (color == 'pink'):
    print('Close!')
else:
    print('Sorry, try again.')
#There seems to have been an additional question for main07.py, but it is not on Canvas or in the README.