#!/usr/bin/python3
"""sends a request and display value of the variable in the header responds"""

if __name__ == "__main__":
    import requests
    from sys import argv

    req = requests.head("https://alx-intranet.hbtn.io", allow_redirects=True)
    print(req.headers['X-Request-Id'])
