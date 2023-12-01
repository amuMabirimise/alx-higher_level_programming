#!/usr/bin/python3
"""
Python script that lists 10 commits (from the most recent to oldest)
of a specified repository by a user using the GitHub API.

Uses the requests and sys packages.
"""

import requests
import sys

if __name__ == '__main__':
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()

        # Displaying information about the latest 10 commits
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Unable to fetch commits. Status code: {response.status_code}")

