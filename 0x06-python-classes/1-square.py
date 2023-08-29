#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """class definition"""
    def __init__(self, size: int) -> None:
        """
        instantiate square with a size attribute
        Args:
            size - size of the square
        """
        self.__size = size
