#!/usr/bin/python3
from base import Base
""" This module holds a derived class of Base """


class Rectangle(Base):
    """ Defines the class Rectangle derieved from Base """

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

    @property
    def x(self) -> int:
        """ retrieves x attribute for validation """
        return self.__x

    @x.setter
    def x(self, data):
        """ validates and set values for x attribute """
        if type(data) != int:
            raise TypeError('x must be an integer')
        if data < 0:
            raise ValueError('x must be >= 0')
        self.__x = data

    @property
    def y(self) -> int:
        """ retrieves y attribute for validation """
        return self.__y

    @y.setter
    def y(self, data):
        """ validates and set values for y attribute """
        if type(data) != int:
            raise TypeError('y must be an integer')
        if data < 0:
            raise ValueError('y must be >= 0')
        self.__y = data

    def area(self) -> int:
        """ Returns area of the rectangle """
        return self.__height * self.__width

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """

        [print('') for y in range(self.y)]
        rect = [' ' * self.x + '#' * self.width for _ in range(self.height)]
        print('\n'.join(rect))

    def __str__(self):
        """ return format: [Rectangle] (<id>) <x>/<y> - <width>/<height>"""

        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ assigns argument and key/value args to each attribute """

        self.id = args[0] if len(args) >= 1 else self.id
        self.__width = args[1] if len(args) >= 2 else self.__width
        self.__height = args[2] if len(args) >= 3 else self.__height
        self.__x = args[3] if len(args) >= 4 else self.__x
        self.__y = args[4] if len(args) >= 5 else self.__y
