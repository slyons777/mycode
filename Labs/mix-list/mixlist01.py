#!/usr/bin/env python3

"""Sarina Lyons | sarina.lyons@tlgcohort.com
   Working with Lists"""

# set up a list
my_list = [ "192.168.0.5", 5060, "UP" ]

# challenge list 
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# display first item 
print("The first item in the list (IP): " + my_list[0] )

# display second item
print("The second item in the list (port): " + str(my_list[1]) )

# display the third item
print("The last item in the list (state): " + my_list[2] )


# print out challenge list
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")

