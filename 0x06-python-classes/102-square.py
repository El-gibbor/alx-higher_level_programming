#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """class definition"""

    def __init__(self, size=0):
        """
            instantiate square with a size attribute
        Args:
            size - size of the square
        raises:
            ValueError - if size is less than 0
            TypeError - if value is not an integer
        """
        self.__size = size

    @property
    def size(self):
        """retrives private instance attribute"""
        return self.__size

    @size.setter
    def size(self, value=0):
        """validate and sets attribute value"""

        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Returns the current square area"""
        return self.__size ** 2

    def __ne__(self, compare_me):
        return self.area() != compare_me.area()

    def __gt__(self, compare_me):
        return self.area() > compare_me.area()

    def __eq__(self, compare_me):
        return self.area() == compare_me.area()

    def __le__(self, compare_me):
        return self.area() <= compare_me.area()

    def __lt__(self, compare_me):
        return self.area() < compare_me.area()

    def __ge__(self, compare_me):
        return self.area() >= compare_me.area()
