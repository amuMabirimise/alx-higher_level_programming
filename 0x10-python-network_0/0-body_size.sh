#!/bin/bash

# Takes a URL as a parameter
url="$1"

# Perform the request and store the response in a temporary file
response_file=$(mktemp)
curl -s -o "$response_file" "$url"

# Get the size of the response body
size=$(stat -c '%s' "$response_file")

# Clean up the temporary file
rm "$response_file"

# Print the size
echo "$size"

