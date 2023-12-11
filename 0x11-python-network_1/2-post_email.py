#!/usr/bin/python3
"""sends a POST request to a URL with email as parameter"""
from urllib import request, parse
from sys import argv


email = argv[2]
arg_val = {'email': email}

data = parse.urlencode(arg_val).encode('ascii')
req = request.Request(argv[1], data)
with request.urlopen(req) as resp:
    print(resp.read().decode('utf-8'))
