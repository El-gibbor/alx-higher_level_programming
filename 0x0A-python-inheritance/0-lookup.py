#!/usr/bin/python3
""" a function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """yields all attributes in the parsed obj"""

    return dir(obj)
