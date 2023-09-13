#!/usr/bin/python3
""" a module containing a derived class of BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines a rectangle, subclass of Geometery """

    def __init__(self, size):
        """ instantiation of instance attributes"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns the area of a rectangle """
        return self.__size * self.__size

    def __str__(self):
        """ return, the below rectangle description:
        [Rectangle] <size>/<size>
        """
        x = "[{}] {}/{}".format(type(self).__name__, self.__size, self.__size)
        return x
