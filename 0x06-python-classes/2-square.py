#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """class definition"""

    def __init__(self, size=0):
        """
        instantiate square with a size attribute
        Args:
            size - size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >=0')
        self.__size = size
