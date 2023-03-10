#!/usr/bin/python3
"""Sarina Lyons | sarina.lyons@tlgcohort.com
   The json.dumps() function creates a JSON string"""

# JSON is part of the Python Standard Library
import json

def main():
    """runtime code"""
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    ## display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## Create the JSON string
    jsonstring = json.dumps(hitchhikers)

    ## Display a single string of JSON
    print(jsonstring)

if __name__ == "__main__":
    main()

