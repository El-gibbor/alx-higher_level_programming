#!/usr/bin/python3
"""a module for python JSON serialization"""
from json import dumps


def to_json_string(my_obj):
    """Returns the JSON representation of an object (str)
    Args:
        my_obj (any object)
    Returns:
        JSON representation of object
    """
    return dumps(my_obj)
