#!/usr/bin/python3
"""This module contains a base class for all models"""
from json import dumps, dump, loads
import os


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
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Square':
            dummy_obj = cls(2)
        else:
            dummy_obj = cls(2, 3)
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """ returns and recreate a list of instances from file """
        if os.path.exists(cls.__name__ + '.json'):
            with open(cls.__name__ + '.json') as from_file:
                file_content = from_file.read()
                deserialised = cls.from_json_string(file_content)
        else:
            return []
        return [cls.create(**obj) for obj in deserialised]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Sertializes in CSV (comma seperated value - e.g Excel)"""
