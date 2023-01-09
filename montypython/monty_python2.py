#!/usr/bin/env python3

"""Sarina Lyons | sarina.lyons@tlgcohort.com
   Monty Python - Using while, if, elif, else"""

round = 0                               # integer initialization
while True:                             # loop set up
    round = round + 1                   # increase counter
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")    # collect input from user
    if answer == 'Brian':               # logic to check if user gave correct answer
        print('Correct!')
        break                           # break statement escapes the while loop
    elif round == 3:                    # check if user has had 3 rounds
        print('Sorry, the answer was Brian.')
        break                           # break statement escapes the while loop
    else:                   # if answer was wrong, and round is not yet equal to 3
        print('Sorry. Try again!')

