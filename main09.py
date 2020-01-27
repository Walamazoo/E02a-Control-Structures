#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

#Line 13 increments count by 1 each time the loop happens.
#Count is a variable that tracks the number of tries the user takes to get the question right.
#Line 23 prints the string, instering count where the {} are.
print('Greetings!')
color = ''
count = 0
while (color != 'red'):
    color = input("What is my favorite color? ")
    color = color.lower().strip()
    count = count + 1               # You can also write this as count += 1
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')

print('You guessed it in {} tries!'.format(count))