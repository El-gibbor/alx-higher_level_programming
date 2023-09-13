#!/usr/bin/python3
"""This module defines a function that adds attributes to objects"""


def add_new_attr(obj, attr_name, value):
    """Add a new attribute to an object if possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
