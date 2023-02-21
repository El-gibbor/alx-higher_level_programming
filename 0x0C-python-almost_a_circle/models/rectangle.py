#!/usr/bin/python3
"""a module that contains a sub class from class, Base """

from models.base import Base


class Rectangle(Base):
    """initializes instance attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes all attributes of rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x-coordinate axis of rectangle
            y (int): y-coordinate axis of rectangle

            Note:
                x and y cordinate of a rectangle can be zero, This is because
                The origin, which is represented by the point(0,0), is where
                x & y axes intersect. so, the setter properties for x & y value
                validates if they're less than 0.
        """

        """call super class so that the base class __init__ logic
        can be used. this is also the id of the class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieves the private attr of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """assign initialised argument to the right attributea value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the private attr of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """assign initialised argument to the right attributea value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieves the private attr of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """assign initialised argument to the right attributea value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves the private attr of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """assign initialised argument to the right attributea value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of rectangle"""
        return self.__height * self.__width
    
    def display(self):
        """Displays the rectangle using # """
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()
