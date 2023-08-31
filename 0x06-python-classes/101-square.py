#!/usr/bin/python3
"""a class Square that defines a square(object)"""


class Square:
    """class definition"""

    def __init__(self, size=0, position=(0, 0)):
        """
            instantiate square with a size attribute
        Args:
            size - size of the square
        raises:
            ValueError - if size is less than 0
            TypeError - if value is not an integer
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrives private instance attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """validate and sets attribute value"""

        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """retrives the position attribute and its value"""
        return self.__position

    @position.setter
    def position(self, value):
        """validates and set value for position attribute"""

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not all(isinstance(i, int) for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')

        if any(elem < 0 for elem in value):
            raise ValueError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square made up of # to stdout"""
        to_stdout = ""
        if self.__size == 0:
            print()
        # the tuple 'position' prints the spaces
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            to_stdout += " " * self.__position[0] + "#" * self.__size + '\n'
        return to_stdout[-1]

    def __str__(self):
        """prints an instance of Square like my_print() func"""
        return self.my_print()
