#!/bin/bash
# This Bash script takes in a URL and displays all HTTP methods the server will accept
curl -si "$1" | awk -F ": " '/Allow/ {print $2}'
