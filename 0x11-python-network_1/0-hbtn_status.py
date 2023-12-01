#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status

Uses the urllib package.
Displays the body of the response with specific information.
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    content = response.read()
    utf8_content = content.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", utf8_content)

