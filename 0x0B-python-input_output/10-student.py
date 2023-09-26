#!/usr/bin/python3
""" Student to JSON with filter """


class Student:
    """a class Student that defines a student by: (based on 9-student.py"""

    def __init__(self, first_name, last_name, age):
        """ initializing public instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance.
        if attrs is a list of strings, only attribute names
        contained in this list must be retrieved. Otherwise,
        all attributes must be retrieved
        """
        if attrs is None or type(attrs) != list:
            return vars(self)  # same as self.__dict__

        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
