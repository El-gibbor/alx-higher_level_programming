#!/usr/bin/python3i
"""a class, Rectangle"""


class Rectangle:
    """defines a rectangle

    Args:
        width(int): width of the rectangle
        height(int): height of the rectangle
    raises:
        TypeError: if height is not an integer
        ValueError: if height is < 0
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialise the instance attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves/return the height attribute"""
        return self.__width

    @height.setter
    def widthself, value):
        """check, validate and set the value for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @property
    def height(self):
        """retrieves/return the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """check, validate and set the value for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
