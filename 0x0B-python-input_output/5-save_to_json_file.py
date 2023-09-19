#!/usr/bin/python3
"""holds a function that writes serialised obj to txt file"""
from json import dump


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""

    with open(filename, 'w') as w_file:
        dump(my_obj, w_file)
