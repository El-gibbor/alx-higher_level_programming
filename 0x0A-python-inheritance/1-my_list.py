#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """superclass -> list, childclass -> Mylist."""
    
    def print_sorted(self):
        """prints list in sorted order"""
        
        print(sorted(self))
