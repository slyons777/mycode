#!/usr/bin/env python3
"""Sarina Lyons | sarina.lyons@tlgcohort.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""

    # create resp, which is our request object
    resp = requests.get("https://api.magicthegathering.io/v1/sets")

    # display the methods available to our new object
    print( dir(resp) )

if __name__ == "__main__":
    main()

