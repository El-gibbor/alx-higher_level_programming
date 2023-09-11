#!/usr/bin/python3
""" module that defines a Geometry """


class BaseGeometry:
    """ defines a class Geometry """

    def area(self):
        """ raises an exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name}  must be greater than 0')
