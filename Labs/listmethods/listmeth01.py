#!/usr/bin/env python3

"""Sarina Lyons | sarina.lyons@tlgcohort.com
   List Methods"""

# set up the list   
proto = ["ssh", "http", "https"]

# print full list
print(proto)

# print second item in list
print(proto[1])

# this line adds d, n, and s
proto.extend("dns")

# reprint list with new extension
print(proto)
