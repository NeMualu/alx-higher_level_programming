#!/bin/bash

# This Bash script sends a DELETE request to the URL passed as the first argument and displays the body of the response

# Send a DELETE request to the specified URL and display the response body
curl -s "$1" -X DELETE

