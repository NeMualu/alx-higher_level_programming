#!/bin/bash
# This Bash script makes a request to the specified URL with a JSON payload and causes the server to respond with a message containing "You got me!" in the body of the response.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
