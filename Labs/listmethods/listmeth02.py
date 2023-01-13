#!/usr/bin/env python3

""" Sarina Lyons | sarinalyons@tlgcohort.com
    Lists, Objects, and Methods Part 2"""


proto = ["ssh", "http", "https"] # set list one
protoa = ["ssh", "http", "https"] # set list two 
print(proto) # print list
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto) # print list one again
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto) # print list one again
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa) # print list two again

proto.remove("ssh") # removing from list
print("Using remove method to substract 'ssh' from proto object, new list appears below.")
print(proto) # print list one again
