#!/usr/bin/python3
"""a class module, rectangle"""


class Rectangle:
    """defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializing instances attributes"""
        self.width = width
        self.height = height
        """Incremented during each new instance instantiation"""
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        ret = ""
        for a in range(self.__height):
            for b in range(self.__width):
                ret += str(self.print_symbol)
            if a is not self.__height - 1:
                ret += ("\n")
        return ret

    def __repr__(self):
        ret = f"Rectangle({self.__width}, {self.__height})"
        return ret

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """retrieving/ return the private attribute for instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """check, validate and set the attribute value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieving/ return the private attribute for instance"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__height + self.__width)
