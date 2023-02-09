#!/usr/bin/python3
"""a class module, BaseGeometry"""


class BaseGeometry:
    """defines a BaseGeometry"""

    def area(self):
        """raises an error if area is checked"""

        raise Exception("area is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer". format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""defines subclass which inherites from BaseGeometry"""


class Rectangle(BaseGeometry):
    """defines subclass which inherites from BaseGeometry"""

    def __init__(self, width, height):
        """using integer_validator() to validate initialised attributes"""

        self.integer_validator(width, height)
        self.__height = height
        self.integer_validator(width, height)
        self.__width = width
