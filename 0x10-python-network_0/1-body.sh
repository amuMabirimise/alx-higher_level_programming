#!/bin/bash
# Usage: ./get_response_body.sh <URL>
# Takes in a URL, sends a GET request to the URL, and displays the body of the response
# Using curl to send a GET request (-X GET), follow redirects (-L), and display the response body (-s)
curl -sX GET "$1" -L

