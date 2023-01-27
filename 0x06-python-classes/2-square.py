#!/usr/bin/python3
"""defining a class, square."""


class Square:

    def __init__(self, size=0):
        """initialising the class, square.
        Args:

            size(int): size of the square

        raises:
            TypeError: if size is not of type int
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
