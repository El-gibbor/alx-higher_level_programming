#!/usr/bin/python3
""" manages urllib.error.HTTPError exceptions """

from urllib import request, parse
from urllib.error import URLError
from sys import argv

try:
    with request.urlopen(argv[1]) as resp:
        print(resp.read().decode('utf-8'))
except URLError as e:
    print(f'Error code: {e.code}')
