#!/usr/bin/python3
"""fetches, displays the value of a variable in the response header"""

import requests
from sys import argv

if __name__ == "__main__":
    print(requests.get(argv[1]).headers['X-Request-Id'])
