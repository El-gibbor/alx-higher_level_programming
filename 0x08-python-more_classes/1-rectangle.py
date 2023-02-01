#!/usr/bin/python3
"""defining a class, rectangle"""


class Rectangle:
    """class with two private attributes"""

    def __init__(self, width=0, height=0):
        """initialising the class

        Args:
            width (int): width of the rectangle. Defaults to 0.
            height (in): height of the Defaults to 0.

        raises:
            TypeError: if width and height are not integers
            ValueError: if width and height are < 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrives the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """checks, validate and set/modify the attribute value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """reetrieves the private attribute value"""
        return self.__height

    @height.setter
    def height(self, value):
        """check, validate and set the value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
