#!/usr/bin/python3
"""
This script sends a request to a given URL and displays the body of the response
(decoded in utf-8). It handles urllib.error.HTTPError exceptions and prints
the HTTP status code in case of an error.
"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
