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

    @width.setter
    def width(self, value):
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

    def area(self):
        """returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle patimeter"""
        return (2 * self.__height + self.width)

    def __str__(self) -> str:
        """defines string representation of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join('#' * self.__width for j in range(self.__height))

    def __repr__(self):
        """returns the representation of a class method that can
        be parsed to create a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1

    def __del__(self, width=0, height=0):
        """destructor, called when all refrences of obj are deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
