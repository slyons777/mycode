#!/usr/bin/env python3
"""Sairna Lyons | sarina.lyons@tlgcohort.com
   Practice with API Slicing"""

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    # find the "sprites" key
    results =  pokeapi["sprites"]["front_default"]
    print(results)

    # loop through moves
    for pokeMove in pokeapi["moves"]:
        print(pokeMove["move"]["name"])

    game_indices = 0

    for g in pokeapi['game_indices']:
        game_indices += 1

    print('This pokemon has appeared in', game_indices, 'video games')

main()

