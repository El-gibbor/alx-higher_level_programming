#!/usr/bin/python3
"""define a square"""


class Square:
    """a square with two private attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """initializing attributes to the class object

        Args:
            size (int): size of object(square). Defaults to 0.
            position (tuple): position of our square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """to retrieve the private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """checks, validate and set the value of square size

        Args:
            value (int): size of the square

        Raises:
            TypeError: if value of size is not an integer
            ValueError: if value of size is < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    @property
    def position(self):
        """retrieves the value for this p-attributes"""
        return self.__position

    @position.setter
    def position(self, value):
        """validate and set the value for our attribute

        Args:
            value (tuple): value for the space/position of square

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if not (isinstance(value, tuple) and len(value) == 2
                and all(isinstance(element, int)
                and element >= 0 for element in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print a square of # character."""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
        for i in range(self.__position[1]):
            print()
