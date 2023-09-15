#!/usr/bin/python3
"""This module contains a base class for all models"""
from json import dumps

class Base:
    """ Defines a base class for all models """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize a new Base
        Args:
            id (int): identification count of a new Base instance
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        else:
            return dumps(list_dictionaries)