#!/bin/bash

# This Bash script takes in a URL and displays all HTTP methods the server will accept

# Send a request to the specified URL and display the HTTP methods allowed by the server
curl -si "$1" | awk -F ": " '/Allow/ {print $2}'

