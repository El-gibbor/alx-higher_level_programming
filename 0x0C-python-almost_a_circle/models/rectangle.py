#!/usr/bin/python3
from base import Base
""" This module holds a derived class of Base """


class Rectangle(Base):
    """ Defines a the class Rectangle derieved from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing instance attributes
        Args:
            width() - width of the rectangle
            height() - height of the rectangle
            x - x axis of the rectangle
            y - y axis of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self) -> int:
        """ retrieves width attribute for validation """
        return self.__width

    @width.setter
    def width(self, data):
        """ validates and set values for width attribute """
        if type(data) != int:
            raise TypeError('width must be an integer')
        if data <= 0:
            raise ValueError('width must be > 0')
        self.__width = data

    @property
    def height(self) -> int:
        """ retrieves height attribute for validation """
        return self.__height

    @height.setter
    def height(self, data):
        """ validates and set values for height attribute """
        if type(data) != int:
            raise TypeError('height must be an integer')
        if data <= 0:
            raise ValueError('height must be > 0')
        self.__height = data

    
