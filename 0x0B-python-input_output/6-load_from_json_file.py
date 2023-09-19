#!/usr/bin/python3
"""convert json to python object"""
import json


def load_from_json_file(filename):
    """t creates an Object from a “JSON file”
       Args:
        filename(json): parameter
    """
    with open(filename) as json_file:
        return (json.load(json_file))
