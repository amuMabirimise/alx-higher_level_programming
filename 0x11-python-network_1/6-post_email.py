#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={'email': email})

    print(response.text)

