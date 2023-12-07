#!/usr/bin/python3
"""sends a request and display value of the variable in the header responds"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    with urllib.request.urlopen(argv[1]) as resp:
        print(resp.info().get('X-Request-Id'))
