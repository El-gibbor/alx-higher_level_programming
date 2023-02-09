#!/usr/bin/python3
"""imports a module to inherit from"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines subclass which inherites from Rectangle"""

    def __init__(self, size):
        """initialize attributes by using a validating
        method(func) from the superclass
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return area of square"""
        return self.__size ** 2

    def __str__(self):
        """prints and return the str replica of the below description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
