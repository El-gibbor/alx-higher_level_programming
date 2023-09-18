#!/usr/bin/python3
def myFunc(**k):
    for key, val in k.items():
        print(f'{key}:{val}')

# dic = {'emekz': 'vic', 'age': 101}

myFunc(a="Real", b="Python", c="Is", d="Great", e="!")

