#!/bin/bash

# This Bash script makes a request to the specified URL with a JSON payload and causes the server to respond with a message containing "You got me!" in the body of the response.

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

# Send a POST request with a JSON payload to the specified URL
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"

