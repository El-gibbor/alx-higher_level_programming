#!/usr/bin/python3
"""Deserializes a JSON file object into a standard python object."""
import json


def save_to_json_file(my_obj, filename):
    """opening the JSON file with python file I/O operation

    Args:
        my_obj (dict): python obj to be serialized
        filename (_type_): where the JSON object will be stored
    """
    with open(filename, "w",) as file:
        json.dump(my_obj, file)
