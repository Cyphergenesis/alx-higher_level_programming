#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using urllib
and displays information about the response body.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode("utf-8")

        print("Body response:")
        print("    - type:", type(body))
        print("    - content:", body)
        print("    - utf8 content:", utf8_content)
