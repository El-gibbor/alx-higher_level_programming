#!/usr/bin/python3
"""imports a module to inherit from"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines subclass which inherites from BaseGeometry"""

    def __init__(self, width, height):
        """using a method from the super class, integer_validator(),
           to validate subclass initialised attributes
        """
        self.integer_validator(height, height)
        self.__height = height
        self.integer_validator(height, height)
        self.__width = width

    def area(self):
        """returns the area of rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """prints/return the str representation of discription below"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
