#!/usr/bin/python3
"""defining a class, square"""


class Square:
    """class that defines a square of private attribute size"""

    def __init__(self, size=0):
        """initialising the class with a private attribute

        Args:
            size (int): size of the square (each instance of class)

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """defining a public instance method, area.

        Returns:
            int: area of the current square
        """
        return self.__size * self.__size
