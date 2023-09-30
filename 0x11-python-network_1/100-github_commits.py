#!/usr/bin/python3
"""
This script fetches the latest commits for a GitHub repository
specified by the owner name and repository name.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"
    response = requests.get(url)

    commits = response.json()
    for commit in commits[:10]:  # Display the latest 10 commits
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")
