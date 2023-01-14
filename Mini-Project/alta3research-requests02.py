#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/"

new_villain = {
           "name": "Doctor Faustus",
           "realName": "Dr. Johann Fennhoff",
           "trivia": "Dr. Fennhoff is seen reading the play The Tragical History of the Life and Death of Doctor Faustus by English playwright Christopher Marlowe during World War II.",
           "quote":"... My greatest weapon has always been my voice... so well modulated and pitched that my very word can either be totally consoling... or destructively jarring!",
            "powers": ["hyponotism","spy","psychology"]
          }

# json.dumps takes a python object and returns it as a JSON string
new_villain = json.dumps(new_villain)

# requests.post requires two arguments at the minimum;
# a url to send the request 
# and a json string to attach to the request
resp= requests.post(URL, json=new_villain)

# pretty-print the response back from our POST request
pprint(resp.json())
