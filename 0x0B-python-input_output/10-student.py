#!/usr/bin/python3
"""a module to serialize the class instance attributes """


class Student:

    def __init__(self, first_name, last_name, age):
        """initializes the class instance attributes to be serialised"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of the class instance

        Args:
            attrs (list(str)): attributes to be returned. Defaults to None.
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
