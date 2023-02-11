#!/usr/bin/python3
"""a model for JSON object deserialization"""
import json


def from_json_string(my_str):
    """returns a JSON object to python standard object"""
    return json.loads(my_str)
