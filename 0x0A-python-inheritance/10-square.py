#!/usr/bin/python3
"""mports a module to inherit from"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """defines subclass that inherit from Rectangle"""

    def __init__(self, size):
         """using a method from the super class, integer_validator(),
         to validate subclass initialised attributes
         """

         self.integer_validator("size", size)
         self.__size = size
         super().__init__(size, size)

    def area(self):
        """returns the area of square"""
        return self.__size * self.__size
