#!/usr/bin/python3
"""a module to serialize the class instance attributes,
desierialize and retrieve key-value pairs of matched attribute names
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """initializes the class instance attributes to be serialised"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of the class instance.
        only key-value pair of class attr name in this list will be retrieved

        Args:
            attrs (list(str)): attributes to be returned. Defaults to None.

        Note:
        The try and except block below might be redundant in this context,
        and its not a mandated requirement from alx. I just added it to handle
        the raised TypeError which is used to cover all edge cases.
        """
        try:
            if attrs is not None and not isinstance(attrs, list):
                raise TypeError
        except TypeError:
            pass
        if attrs is None:
            return vars(self)
        elif all(isinstance(values, str) for values in attrs):
            result = {}
            for values in attrs:
                if hasattr(self, values):
                    result[values] = getattr(self, values)
            return result
    
    def reload_from_json(self, json):
        for keyz, valz in json.items():
            if hasattr(self, keyz):
                setattr(self, keyz, valz)
