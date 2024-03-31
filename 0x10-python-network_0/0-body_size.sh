#!/bin/bash
# This Bash script takes in a URL, sends a GET request to that URL, and displays the size of the body of the response

curl -sI "$1" | awk '/Content-Length/ {print $2}'
