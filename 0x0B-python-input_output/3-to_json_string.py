"""a module for python JSON serialization"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (str)"""
    return json.dumps(my_obj)