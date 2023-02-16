#!/usr/bin/python3
"""this module defines a function that return the dictionary description
or representation of a parsed in instance of a class(obj)
"""


def class_to_json(obj):
    return vars(obj)
