#!/usr/bin/python3
""" contains a func that converts to json"""
from json import dumps


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""

    return dumps(my_obj)
