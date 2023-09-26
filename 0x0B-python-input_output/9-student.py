#!/usr/bin/python3
""" Student to Json """


class Student:
    """ a class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ initializing public instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance.
        vars() method returns the __dict__ (dictionary mapping) attribute of
        the given object, same as self.__dict__
        """
        return vars(self)
