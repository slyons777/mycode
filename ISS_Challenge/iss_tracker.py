#!/usr/bin/env python3
"""Sarina Lyons | sarina.lyons@tlgcohort.com
   Returning the location of the ISS in latitude/longitude"""

import requests
import datetime

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]

    print(f"""
    CURRENT LOCATION OF THE ISS:
    Lon: {lon}
    Lat: {lat}
    """)

    time = resp["timestamp"]
    time = datetime.datetime.fromtimestamp(time)

    print(f"""
    CURRENT LOCATION OF THE ISS:
    Timestamp: {time}
    Lon: {lon}
    Lat: {lat}
    """)

if __name__ == "__main__":
    main()

