#!/bin/bash

# This Bash script sends a request to a specified URL and displays the size of the response body

# Extract the content length from the response headers using curl and awk
content_length=$(curl -sI "$1" | awk '/Content-Length/ {print $2}')

# Print the content length
echo "Content Length: $content_length"

