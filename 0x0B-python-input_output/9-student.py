#!/usr/bin/python3
"""A module with a function that returns the dictionary representation
of all instance attributes of the class.
"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns all attributes of the class instance in dict"""
        return vars(self)
