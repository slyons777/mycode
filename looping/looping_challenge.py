#!usr/bin/env python3

"""Sarina Lyons | sarina.lyons@tlgcohort.com
   looping CHALLENGE
"""

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
        {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# returns all animals from NE farm
for farm in farms:
    if farm["name"] == "NE Farm":
        for agriculture in farm["agriculture"]:
            print(agriculture)

# asks user to choose a farm then returns animals on that farm
chosen_farm = input("Please choose a farm (NE Farm, W Farm, or SE Farm): ")

for farm in farms:
    if farm["name"] == chosen_farm:
        for agriculture in farm["agriculture"]:
            print(agriculture)

# returns animals ONLY from the farm user picked
chosen_farm = input("Please choose a farm (NE Farm, W Farm, or SE Farm): ")

for farm in farms:
    if farm["name"] == chosen_farm:
        for agriculture in farm["agriculture"]:
            if agriculture in ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]:
                print(agriculture)


