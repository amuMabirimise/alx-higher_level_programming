#!/usr/bin/python3

import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) != 3:
        print("Usage: {} <repository_name> <owner_name>".format(argv[0]))
        exit(1)

    repository_name = argv[1]
    owner_name = argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()

        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Unable to fetch commits. Status code: {response.status_code}")

