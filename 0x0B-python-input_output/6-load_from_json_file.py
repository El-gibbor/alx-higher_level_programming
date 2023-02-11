#!/usr/bin/python3
"""a module for object creation fromM json file"""
import json


def load_from_json_file(filename):
    """open and return a deserialized JSON file object"""
    with open(filename) as file:
        return json.load(file)
