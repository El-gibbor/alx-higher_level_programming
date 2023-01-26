#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    A class that defines a square by
    the private attribute, size
    """

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): the size of the square
        """
        self.__size = size
