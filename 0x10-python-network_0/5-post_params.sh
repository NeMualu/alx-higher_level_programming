#!/bin/bash

# This Bash script takes in a URL, sends a POST request to the passed URL, and displays the body of the response.

# Send a POST request to the specified URL with data and display the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"

