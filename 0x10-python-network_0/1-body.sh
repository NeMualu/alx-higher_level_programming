#!/bin/bash
# This Bash script takes in a URL, sends a GET request to the URL, and displays the body of the response
# Using curl to send a GET request to the provided URL and following redirections, then outputting the HTTP status code
curl -sIL "$1" | grep -E "^HTTP" | tail -n1 | awk '{print $2}'
