#!/usr/bin/python3
"""define a class, square"""


class Square:
    """difinimg a class with private attribute"""

    def __init__(self, size=0):
        """initialises the instace, Square

        Args:
            size(int): size of the square

        raise:
            TypeError: if size is not an integer
            ValuError: if size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """retrives the attribute

        returns:
            size: object private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of private attribute

        Args:
            value(int): size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints a square of char "#"""
        if self.size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
