#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """
from urllib import request

with request.urlopen("https://alx-intranet.hbtn.io/status") as fetched:
    response = fetched.read()

    print("Body response:")
    print(f"\t- type: {type(response)}")
    print(f"\t- content: {response}")
    print(f"\t- utf8 content: {response.decode('utf8')}")
