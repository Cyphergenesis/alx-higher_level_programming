#!/usr/bin/python3
"""
This script sends a POST request to a given URL with an email parameter and
displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data)

    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.URLError as e:
        print("Error:", e.reason)
        sys.exit(1)

    print("Your email is:", email)
