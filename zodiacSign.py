#!/usr/bin/python3

# This is an app designed to tell a user their zodiac sign, based on their birtdate. # User will be prompted to enter birth day and month and their zodiac sign should be # printed to the screen. Error checking should be done to ensure user is entering 
# appropriate characters depending upon input prompt i.e. (letters for name, numbers # for date)

def main():
    # Welcome user and prompt for name
    user_name = input("Welcome to SunSigns! What's your name? ")

    # prompt for month, day
    month = input("Thanks! Now how about your birth month?").lower()
    day = int(input("Now the day? "))

    # check against month and date input to get sign
    if month == 'december':
	    zodiac_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 'january':
	    zodiac_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 'february':
	    zodiac_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 'march':
	    zodiac_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 'april':
	    zodiac_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 'may':
	    zodiac_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month == 'june':
	    zodiac_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 'july':
	    zodiac_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 'august':
	    zodiac_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 'september':
	    zodiac_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 'october':
	    zodiac_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 'november':
	    zodiac_sign = 'scorpio' if (day < 22) else 'Sagittarius'

    print("Awesome looks like you're a " + zodiac_sign + "!")

if __name__ == "__main__":
    main()
