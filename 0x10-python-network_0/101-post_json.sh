#!/bin/bash
# Bash script that sends a JSON POST request to a URL
curl -X POST -H "Content-Type: application/json" -d "$(cat $2)" $1 -s -o /dev/null && echo "Valid JSON" || echo "Not a valid JSON"
