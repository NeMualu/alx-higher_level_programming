#!/bin/bash

# This Bash script sends a GET request to a specified URL and displays the body of the response if the status code is 200

# Send a HEAD request to check the status code
status_code=$(curl -sLI "$1" -X GET | awk 'NR==1{print $2}')

# Check if the status code is 200
if [ "$status_code" = '200' ]; then
    # If the status code is 200, send a GET request and display the body of the response
    curl -sL "$1"
fi

