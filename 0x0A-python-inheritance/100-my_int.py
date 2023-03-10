#!/usr/bin/python3
"""class module that inherits from int"""


class MyInt(int):
    """ module of a rebel class that returns the negation of a given comparison
        operator.
        == and != operators are defined to return an inverted behaviour
    """
    def __eq__(self, other):
        """== operator is inverted to the opposite of what it does"""
        return self != other

    def __ne__(self, other):
        """!= operator is inverted to the opposite of what it does"""
        return self == other
