#!/usr/bin/python3

"""Sarina Lyons | sarina.lyons@tlgcohort.com
   Write your own if-logic script - Zodiac Sign"""

# This is an app designed to tell a user their zodiac sign, based on their birtdate. # User will be prompted to enter birth day and month and their zodiac sign should be # printed to the screen. Error checking should be done to ensure user is entering 
# appropriate characters depending upon input prompt i.e. (letters for name, numbers # for date)

def determine_zodiac(month, day):
  # Dictionary mapping zodiac signs to start and end dates
  zodiac_dates = {
    "Aries": (3, 21, 4, 19),
    "Taurus": (4, 20, 5, 20),
    "Gemini": (5, 21, 6, 20),
    "Cancer": (6, 21, 7, 22),
    "Leo": (7, 23, 8, 22),
    "Virgo": (8, 23, 9, 22),
    "Libra": (9, 23, 10, 22),
    "Scorpio": (10, 23, 11, 21),
    "Sagittarius": (11, 22, 12, 21),
    "Capricorn": (12, 22, 1, 19),
    "Aquarius": (1, 20, 2, 18),
    "Pisces": (2, 19, 3, 20)
  }

  # Iterate through the dictionary until we find the correct zodiac sign
  while True:
    for sign, dates in zodiac_dates.items():
      start_month, start_day, end_month, end_day = dates
      if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
        return sign

# Prompt the user to enter their birthday
birthday = input("Please enter your birthday (MM/DD): ")

# Split the birthday into the month and day
month, day = map(int, birthday.split("/"))

# Determine the user's zodiac sign
sign = determine_zodiac(month, day)

# Print the user's zodiac sign
print(f"Awesome your zodiac sign is: {sign}")


if __name__ == "__determine_zodiac__":
    determine_zodiac()
