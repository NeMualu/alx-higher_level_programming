#!/bin/bash
# This Bash script takes in a URL, sends a GET request to the URL, and displays the body of the response
# Using curl to send a GET request to the provided URL and following redirections
curl -sL "$1" -o /dev/null -w "%{http_code}"
