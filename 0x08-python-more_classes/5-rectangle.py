#!/usr/bin/python3
"""a class, Rectangle"""


class Rectangle:
    """a rectangle with two private attributes

    Args:
        width(int): the rectangle width
        height(int): the rectangle height

    raises:
        TypeError: if width or height is not an integer
        ValueError: if width or heigth is < 0
    """

    def __init__(self, width=0, height=0):
        """initializing the instance attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves/return the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """check, validate and set the width attribute

        Args:
            value(int): value/size of the rectangle width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves/return the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """check, validate and set the width attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle parimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """prints the str representation of rectangle with # char"""
        if self.__width == 0 or self.__heigth == 0:
            return ""
        ret_str = ""
        for i in range(self.__width):
            for j in range(self.__height):
                ret_str += "#"
            ret_str += "\n"
        return (ret_str[:-1])

    def __repr__(self):
        """returns the representation of a clas method that can
        be parsed to create a new instance
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """destructor, called when all refrences of obj are deleted"""
        print("Bye rectangle...")
