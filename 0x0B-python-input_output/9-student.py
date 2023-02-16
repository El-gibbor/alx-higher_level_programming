#!/usr/python3
"""This module defines a class & a method that retrieves a dictionary
representation of the class instance.

Returns:
   dict: 
"""


class Student:
    """defines a class, Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dict representation of all instance attributes of the class, Student"""
        return (self.__dict__)
