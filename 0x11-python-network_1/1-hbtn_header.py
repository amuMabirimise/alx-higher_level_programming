#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the header of the response.

Uses the urllib and sys packages.
"""

import urllib.request
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.info().get('X-Request-Id')
        print(x_request_id)
else:
    print("Usage: {} <URL>".format(sys.argv[0]))

