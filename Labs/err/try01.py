#!/usr/bin/python3
"""Sarina Lyons | sarina.lyons@tlgcohort.com
   Review of try and catch logic"""

# Start with an infinite loop
while True:
    try:
        print("Enter a file name: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("No problems with that file name.")
        break
    except:
        print("Error with that file name! Try again...")

