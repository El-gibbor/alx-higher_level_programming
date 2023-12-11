#!/usr/bin/python3
"""displays the error code of URL response if it is greater than 400"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
