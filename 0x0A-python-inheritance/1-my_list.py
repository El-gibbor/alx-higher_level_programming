#!/usr/bin/python3
""" a function that returns the list of available attributes
and methods of an object
"""


class MyList(list):
    """superclass -> list, childclass -> Mylist."""
    
    def print_sorted(self):
        """prints list in sorted order"""
        print(sorted(self))
