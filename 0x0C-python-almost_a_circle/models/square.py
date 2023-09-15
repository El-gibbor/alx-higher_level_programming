#!/usr/bin/python3
""" module holding a Derived class of Rectangle """
from rectangle import Rectangle


class Square(Rectangle):
    """ Defines the derived class of Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes instance attributes with superclass __init__ logic"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ inherits the validation logic of superclass """
        return self.width

    @size.setter
    def size(self, data):
        """ validates value with the superclass logic """
        self.width = data
        self.height = data

    def __str__(self):
        """ returning the class attributes in the below format """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Assigns instance attributes """

        len_arg = len(args)
        if args:
            self.id = args[0] if len_arg >= 1 else self.id
            self.size = args[1] if len_arg >= 2 else self.size
            self.x = args[2] if len_arg >= 3 else self.x
            self.y = args[3] if len_arg >= 4 else self.y
        else:
            for attr, val in kwargs.items():
                setattr(self, attr, val)
