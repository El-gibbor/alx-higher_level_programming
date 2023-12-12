#!/usr/bin/python3
"""sends a POST request to a URL with letter as parameter"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    arg_val = argv[1] if len(argv) > 1 else ""
    the_data = {"q": arg_val}

    try:
        r = requests.post(url, data=the_data)
        if r.json():
            print(f"[{r.json()['id']}] {r.json()['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
