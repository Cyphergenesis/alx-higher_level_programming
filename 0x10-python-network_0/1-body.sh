#!/bin/bash
#  takes in a URL, sends a GET request to the URL
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
