#!/usr/bin/python

"""Sarina Lyons | sarina.lyons@tlgcohort.com
   Challenge:Dictionaries (Characters)"""

marvelchars= {
    "Starlord":
    {"real name": "peter quill",
    "powers": "dance moves",
    "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
    "powers": "shape shifter",
    "archenemy": "Professor X"},

    "Hulk":
    {"real name": "bruce banner",
    "powers": "super strength",
    "archenemy": "adrenaline"}
    }

while True:
  char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)")
  char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")

  char_name = char_name.capitalize()  # Capitalize the character name to ensure that it matches the keys in the dictionary
  char_stat = char_stat.lower()  # Lowercase the statistic name to ensure that it matches the keys in the dictionary

  if char_name in marvelchars and char_stat in marvelchars[char_name]:
    value = marvelchars[char_name][char_stat]
    if char_stat == "real name":
      value = value.capitalize()  # Capitalize the real name
    print(f"{char_name}'s {char_stat} is: {value}")
  else:
    print("I'm sorry, I couldn't find that information. Please try again.")



