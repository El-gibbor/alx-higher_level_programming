#!/usr/bin/python3
""" holds a function that converts back to python obj"""
from json import loads


def from_json_string(my_str):
    """ returns an object (Python data structure)
    represented by a JSON string
    """
    return loads(my_str)
