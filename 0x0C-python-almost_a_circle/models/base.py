#!/usr/bin/python3
"""a module for the class Base of all other classes in this project"""
from json import dumps


class Base:
    """defines the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """serialises contents of list_dictionaries (list_of_dict to json)"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return dumps(list_dictionaries)
