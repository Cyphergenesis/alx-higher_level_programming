#!/usr/bin/python3
"""
This script sends a request to a given URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, it prints an error message.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    response = requests.get(url)
    content = response.text

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(content)
