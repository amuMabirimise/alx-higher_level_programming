#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code:", e.response.status_code)

