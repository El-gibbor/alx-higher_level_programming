#!/usr/bin/python3
"""define a rectangle"""


class Rectangle:
    """# character representation of a rectangle

    Args:
        height(int): length of the rectangle
        width(int): width size of the rectangle

    raises:
        TypeError: if height or width is not an integer
        VAlueError: if the value of heigth or width is < 0
        """
    def __init__(self, width=0, height=0):
        """initialising the instance attribuutes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retreives/returns the the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """checks, validate and set the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retreives/returns the the value of width"""
        return self.__height

    @height.setter
    def height(self, value):
        """checks, validate and set the width attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """retunrs the rectangle parimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """string representation to print a rectangle of # character"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return_str = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    return_str += "#"
                return_str += "\n"
            return (return_str)
