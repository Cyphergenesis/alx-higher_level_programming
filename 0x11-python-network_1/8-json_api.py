#!/usr/bin/python3
"""
This script sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter and processes the response.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        q = ""
    else:
        q = sys.argv[1]

    payload = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'

    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
