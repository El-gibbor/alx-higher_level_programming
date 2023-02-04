#!/usr/bin/python3
"""square module that compares its instances"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """initializing instance attributes

        Args:
            size (int): size square instance(object). Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """retrieve/return the size of object"""
        return self.__size

    @size.setter
    def size(self, value):
        """check, validate and set the value of instance attribute"""
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the currrent area square"""
        return self.__size ** 2

    def __eq__(self, other):
        """compares if square is equal to other"""
        return self.__size == other.__size

    def __ne__(self, other):
        """compares if square is not equal to other"""
        return self.__size != other.__size

    def __gt__(self, other):
        """compares if square is greater than to other"""
        return self.__size > other.__size

    def __ge__(self, other):
        """compares if square is >= to other"""
        return self.__size >= other.__size

    def __le__(self, other):
        """compares if square is <= to other"""
        return self.__size <= other.__size

    def __lt__(self, other):
        """compares if square is < other"""
        return self.__size < other.__size
