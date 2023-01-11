#!/usr/bin/env python3
"""Sarina Lyons | sarina.lyons@tlgcohort.com
   Trivia Game API Challenge"""

import requests

URL= 'https://opentdb.com/api.php?amount=10'

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()

    for category in data['results']:
        print(['results']['category'])


if __name__ == "__main__":
    main()
