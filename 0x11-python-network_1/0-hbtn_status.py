#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status

Uses the urllib package.
Displays the body of the response with specific information.
"""

import urllib.request as request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as r:
        html = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
