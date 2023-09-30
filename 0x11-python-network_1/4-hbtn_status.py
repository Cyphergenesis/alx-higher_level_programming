#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using the requests library
and displays information about the response body.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    
    response = requests.get(url)
    content_type = response.headers.get('content-type')
    content = response.text

    print("Body response:")
    print("    - type:", type(content))
    print("    - content:", content)
