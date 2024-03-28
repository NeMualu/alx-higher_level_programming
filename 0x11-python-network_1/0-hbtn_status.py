#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib
"""

import urllib.request

def main():
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        html_content = response.read()
        utf8_content = html_content.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(html_content))
    print("\t- content:", html_content)
    print("\t- utf8 content:", utf8_content)

if __name__ == "__main__":
    main()

