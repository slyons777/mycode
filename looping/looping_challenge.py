"""Sarina Lyons | sarina.lyons@tlgcohort.com
   looping CHALLENGE
"""

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
        {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

NE_animals = farms[0]["agriculture"]

for x in NE_animals:
     print(x)

