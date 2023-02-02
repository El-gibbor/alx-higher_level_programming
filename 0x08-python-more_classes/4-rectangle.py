!usr/bin/python3
"""a class, rectangle"""


class Rectangle:
    """
    a rectangle with to attributes

    Args:
        withds(int): width of rectangle
        height(int): height of rectangle
    """
    def __init__(self, width=0, height=0):
        """initializing the class with two private instance attr."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retriev/return the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """check, validate and set the width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve/return the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """check, validate and set the height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """retuns the rectangle parimeter"""
        return (2 * (self.width + self.__height))

    def __str__(self):
        """str representation of the class which prints rectangle of # char"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            str_return = ""
            for i in range(self.__width):
                for j in range(self.__height):
                    str_return += "#"
                str_return += "\n"
            return (str_return[:-1])

    def __repr__(self):
        """returns the representation of a clas method that can
        be parsed to create a new instance
        """
        return "Rectangle({}, {})".format(self.width, self.height)
