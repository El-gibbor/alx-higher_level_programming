#!/usr/bin/python3
"""defining a class, rectangle"""


class Rectangle:
    """class with two private attributes"""

    def __init__(self, width=0, height=0):
        """initialising the class"""
        self.width = width
        self.height = height

    @property
    def width(self, value):
        """retrives the private attribute value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        return self.__value

    @width.setter
    def width(self, value):
        """checks, validate and set/modify the attribute value"""
        self.__value = value

    @property
    def height(self, VALUE):
        """reetrieves the private attribute value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, value):
        """check, validate and set the value"""
        self.__value = value
