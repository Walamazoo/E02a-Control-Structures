#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

#This program is different because it accepts multiple correct answers.
#This is trying to solve the issue of users not capitalizing.
print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red' or color == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')
#If another capitilization squeme is used, it is treated as wrong.
#This tells us the color must be an exact macth to be correct.