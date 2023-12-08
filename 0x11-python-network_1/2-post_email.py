#!/usr/bin/python3
"""sends a POST request to a URL with email as parameter"""
import urllib.parse
import urllib.request
from sys import argv


email = argv[2]
arg_val = {'email': email}
data = urllib.parse.urlencode(arg_val).encode('ascii')
# data = data.encode('ascii')
req = urllib.request.Request(argv[1], data)
with urllib.request.urlopen(req) as resp:
    print(resp.read().decode('utf-8'))
