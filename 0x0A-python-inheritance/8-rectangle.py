#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" a modeul containing a derived class of BaseGeometry"""


class Rectangle(BaseGeometry):
    """ defines a rectangle, subclass of Geometery """

    def __init__(self, width, height):
        """ instantiation of instance attributes"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
