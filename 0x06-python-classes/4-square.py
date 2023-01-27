#!/usr/bin/python3
"""difine a class, square"""


class Square:
    """class with private attribute, size"""

    def __init__(self, size=0):
        """initializing the class, square with it's attributes

        Args:
            size (int): size of the square

        raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """retrieve the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of the attribute, size.

        Args:
            value (int): new size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)
