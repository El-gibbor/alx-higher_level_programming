#!/usr/bin/python3
"""a module for object creation from json file"""
from json import load


def load_from_json_file(filename):
    """open and return a deserialized (python obj) JSON file object"""
    with open(filename) as file:
        return load(file)
