#!/usr/bin/python3
"""a class Square that defines a square(object)"""


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

    def my_print(self):
        """prints the square made up of # to stdout"""

        if self.__size == 0:
            print()

        # convert to 3x3 matrix of "#" and print them literally without a list
        sqr = [['#' for _ in range(self.__size)] for _ in range(self.__size)]
        for each_row in sqr:
            print(''.join(each_row))
