#!/usr/bin/python3
""" This module holds a derived class of Base """
from base import Base


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
    def width(self):
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
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[2] if len(args) >= 3 else self.height
            self.x = args[3] if len(args) >= 4 else self.x
            self.y = args[4] if len(args) >= 5 else self.y
        else:
            for keys, val in kwargs.items():
                setattr(self, keys, val)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""

        to_dict = {}
        for attr in ['id', 'width', 'height', 'x', 'y']:
            to_dict[attr] = getattr(self, attr)
        return to_dict
