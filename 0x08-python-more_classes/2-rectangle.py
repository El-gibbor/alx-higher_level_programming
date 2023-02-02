#!/usr/bin/python3
"""defining a Rectangle"""


class Rectangle:
    """a rectangle wit two private attributes

    Args:
        width(int): width size of the rectangle
        height(int): height of the rectangle.

    raises:
        TypeError: if width or height is not an integer
        ValueError: if width or height is less than 0
        """
    def __init__(self, width=0, height=0):
        """initialise object private attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrive the value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """check, validate and modify/set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrives the value for width"""
        return self.__height

    @height.setter
    def height(self, value):
        """check, validate and modify/set the width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
