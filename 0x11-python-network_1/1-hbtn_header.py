#!/usr/bin/python3
"""
This script sends a request to a given URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            header = response.headers.get("X-Request-Id")
            if header:
                print(header)
    except urllib.error.URLError as e:
        print("Error:", e.reason)
        sys.exit(1)
