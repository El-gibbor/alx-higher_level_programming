#!/usr/bin/python3
"""a model for JSON object deserialization"""
from json import loads


def from_json_string(my_str):
    """returns a JSON object to python standard object"""
    return loads(my_str)
