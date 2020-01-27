#!/usr/bin/env python3
import sys, random #Imports the random class.

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!') #Prints Greetings!
colors = ['red','orange','yellow','green','blue','violet','purple'] #Creates a list with a variety of strings.
play_again = '' #Initializes play_again
best_count = sys.maxsize #Initializes best_count with the biggest number

while (play_again != 'n' and play_again != 'no'): #Loops the code in its block according to the conditions.
    match_color = random.choice(colors) #Sets match_color to a random string from the list.
    count = 0 #Initializes count to 0.
    color = '' #Initializes color
    while (color != match_color): #Loops the code in its block according to the conditions.
        color = input("\nWhat is my favorite color? ") #\n is a special code that adds a new line. Prints the string and assigns the input to color.
        color = color.lower().strip() #Makes color lowercase and removes extra spaces.
        count += 1 #Increments count by 1.
        if (color == match_color): #Runs the block of code if the condition is met.
            print('Correct!') #Prints the string.
        else: #Runs the block of code if privious the condition was not met.
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #Prints the string, inserting count where the {} are.
    
    print('\nYou guessed it in {} tries!'.format(count)) #Prints the string, inserting count where the {} are.

    if (count < best_count): #Runs the block of code if the condition is met.
        print('This was your best guess so far!') #Prints the string.
        best_count = count #Assigns count to best_count.

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() #Prints the string, makes the input lowercase and removes extra spaces, and assigns it to play_again.

print('Thanks for playing!') #Prints the string.