#!/usr/bin/python3
"""This module defines a function that adds attributes to objects"""


def add_attr(obj, attr_name, attr_value):
    """
    Args:
        obj (object): The object to which the attribute should be added.
        attr_name (str): The name of the attribute to be added.
        attr_value (any): The value of the attribute to be added.
    Raises:
        TypeError: If the object doesn't have a '__dict__' attribute,
        indicating it's not possible to add attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
