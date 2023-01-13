#!/usr/bin/env python3

"""Sarina Lyons | sarina.lyons@tlgcohort.com
   Testing If conditionals"""

# Check hostname against expected value

## Collect input from user
hostname = input("What value should we set for hostname?")

## use the lower method to test matching value
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

## Always display to the user
print("Exiting the script")


