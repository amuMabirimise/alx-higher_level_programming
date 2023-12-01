#!/usr/bin/python3
'''
Displays X-Request-Id value from response header.
'''

import urllib.request as req
import sys

if __name__ == "__main__":
    with req.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))

