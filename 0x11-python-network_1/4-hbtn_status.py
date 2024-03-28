#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using requests
"""

import requests

def main():
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

if __name__ == "__main__":
    main()

