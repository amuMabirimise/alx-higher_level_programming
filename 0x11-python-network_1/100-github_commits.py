#!/usr/bin/python3
"""GitHub commits code challenge"""

import requests
from sys import argv

if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided
    if len(argv) != 3:
        print("Usage: {} <owner> <repo>".format(argv[0]))
        exit(1)

    owner = argv[1]
    repo = argv[2]

    # Construct the URL for the GitHub API request
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        commits = response.json()

        # Display information about the latest 10 commits
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Unable to fetch commits. Status code: {response.status_code}")

