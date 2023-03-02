#!/usr/bin/python3
"""a module for the class Base of all other classes in this project"""
from json import dumps, loads


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
        if list_dictionaries is None:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        listz = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as file:
            if list_objs:
                for values in list_objs:
                    listz.append(values.to_dictionary())
            file.write(cls.to_json_string(listz))

    @staticmethod
    def from_json_string(json_string):
        """returns the list represented by json_str (json to python(list))"""
        return loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set by creating a
        dummy instance as a placeholder for the actual instance attr and values
        """
        if cls.__name__ == "Rectangle":
            dummy_cls_obj = cls(5, 8)
        if cls.__name__ == "Square":
            dummy_cls_obj = cls(9)
        dummy_cls_obj.update(**dictionary)
        return dummy_cls_obj
