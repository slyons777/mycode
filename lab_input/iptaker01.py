#!/usr/bin/env python3
"""Sarina Lyons | sarina.lyons@tlgcohort.com
   Collecting user input()"""

# below is a function containing our code
def main():

    # pause the program and wait for the user to provide input
    user_input = input("Please enter an IPv4 IP address:")
    
    # display the input back to the user.
    print("You told me the IPv4 address is: " + user_input)
    
    # ask for vendor name
    vendor = input("Please include the vendor name: ")
    print(vendor)
# this calls main

main()
