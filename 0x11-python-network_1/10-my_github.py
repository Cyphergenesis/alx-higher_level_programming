#!/usr/bin/python3
"""
This script uses Basic Authentication with a personal access token to access
your GitHub information and display your id.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        data = response.json()
        print(data.get('id'))
    else:
        print(None)
