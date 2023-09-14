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
