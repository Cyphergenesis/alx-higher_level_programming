#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -s -X POST -H "Content-Type: application/json" --data @"$2" "$1" | jq -e . >/dev/null && cat "$2" || echo "Not a valid JSON"
