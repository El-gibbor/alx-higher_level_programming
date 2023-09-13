#!/usr/bin/python3
""" A module containing a derived class of int"""


class MyInt(int):
    """ Defines a derieved class of int """

    def __eq__(self, date):
        """Override == opeartor with != """
        return self.real != date

    def __ne__(self, date):
        """Override != operator with == """
        return self.real == date
