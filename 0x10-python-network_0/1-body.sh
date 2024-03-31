#!/bin/bash
# This Bash script takes in a URL, sends a GET request to the URL, and displays the body of the response
response=$(curl -sIL "$1" -o /dev/null -w "%{http_code}")
if [ "$response" = '200' ]; then
    echo "no redirection"
elif [ "$response" = '301' ]; then
    echo "1 redirection"
else
    echo "5 redirection with multiple status code"
fi
