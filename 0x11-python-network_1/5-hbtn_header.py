#!/usr/bin/python3
"""fetches, displays the value of a X-Request-Id in the response header"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers['X-Request-Id'])
