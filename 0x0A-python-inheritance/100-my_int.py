#!/usr/bin/python3
""" A module containing a derived class of int"""


class MyInt(int):
    """ Defines a derieved class of int """

    def __eq__(self, value):
        """Override == opeartor with != """
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == """
        return self.real == value