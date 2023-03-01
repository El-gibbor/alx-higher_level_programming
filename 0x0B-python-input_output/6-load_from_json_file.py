#!/usr/bin/python3
"""Deserializes a JSON file object into a standard python object."""
from json import load


def load_from_json_file(filename):
    """open and return a deserialized (python obj) from JSON file object"""
    with open(filename) as file:
        return load(file)
