#!/bin/bash

# This Bash script sends a request to a URL passed as an argument and displays only the status code of the response.

# Send a request to the URL and output only the status code
curl_status=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Display the status code
echo "$curl_status"

