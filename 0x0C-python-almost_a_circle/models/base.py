#!/usr/bin/python3
"""This module contains a base class for all models"""
from json import dumps, dump, loads


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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        with open(cls.__name__ + '.json', 'w') as j_file:
            if list_objs is None:
                j_file.write('[]')
            else:
                serialised = [objs.to_dictionary() for objs in list_objs]
                j_file.write(cls.to_json_string(serialised))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation (json_string)"""
        json_to_dict = []
        if json_string or json_string is not None:
            if not isinstance(json_string, str):
                raise TypeError('json_string must be a string')
            json_to_dict = loads(json_string)
        return json_to_dict

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy_inst = cls(2, 3, 1, 1)
        dummy_inst.update(**dictionary)
        return dummy_inst
