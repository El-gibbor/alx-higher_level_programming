#!/usr/bin/python3
"""dumps a serialised python object into a file."""
from json import dump


def save_to_json_file(my_obj, filename):
    """opening the JSON file to written into with python file I/O operation

    Args:
        my_obj (dict): python obj to be serialized
        filename (_type_): where the JSON object will be stored
    """
    with open(filename, "w",) as file:
        dump(my_obj, file)
