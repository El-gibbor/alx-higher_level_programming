#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""

import requests
from sys import argv

if __name__ == "__main__":
    url, email = argv[1], argv[2]

    r = requests.post(url, data={'email': email})
    print(r.text)
