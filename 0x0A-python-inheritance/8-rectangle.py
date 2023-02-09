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
        self.integer_validator(width, width)
        self.__width = width
