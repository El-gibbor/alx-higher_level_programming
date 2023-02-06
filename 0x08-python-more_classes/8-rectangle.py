#!/usr/bin/python3i
"""class module, rectangle"""


class Rectangle:
    """defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes unstatnce attributes"""
        self.width = width
        self.height = height
        """increamented when an instance is created"""
        Rectangle.number_of_instances += 1

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        ret = ""
        for a in range(self.height):
            ret += str(self.print_symbol) * self.width + "\n"
        return ret[:-1]

    def __repr__(self):
        """return a string representation of the rectangle"""
        ret = f"Rectangle({self.__width}, {self.__height})"
        return ret

    def __del__(self):
        """Decremented during each instance deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """retrieve/ return the width"""
        return self.__width

    @width.setter
    def width(self, k):
        """check, valiate and set the value for width"""
        if type(k) is not int:
            raise TypeError("width must be an integer")
        if k < 0:
            raise ValueError("width must be >= 0")
        self.__width = k

    @property
    def height(self):
        """retrieve/return the height attribute"""
        return self.__height

    @height.setter
    def height(self, k):
        """check, validate and set the height attribute"""
        if type(k) is not int:
            raise TypeError("height must be an integer")
        if k < 0:
            raise ValueError("height must be >= 0")
        self.__height = k

    def area(self):
        """return the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """return the paremeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2*(self.__height + self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
