#!/usr/bin/python3
""" fetches the content of a URL using reuests package"""

import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print(f"- type: {type(r.text)}")
print(f"- content: {r.text}")
