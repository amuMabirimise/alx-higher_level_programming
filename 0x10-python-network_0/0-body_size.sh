#!/bin/bash
# Usage: ./get_body_size.sh <URL>
# Request a URL and display the size of the body of the response
# Using curl to fetch the response headers, grep for Content-Length, and extract the size
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

