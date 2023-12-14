#!/usr/bin/python3
"""Basic Auth with Github API to display user id"""

import requests
from sys import argv
from requests import auth

if __name__ == "__main__":
    r = requests.get('http://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json()['id'])
