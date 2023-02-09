#!/usr/bin/python3
"""class module that inherits from int"""


class MyInt(int):
    """ a rebel class that returns the negation of the given operators.
        == and != operators are defined to return and inverted behaviour
    """
    def __eq__(self, other):
        """inverts == operator to the opposite of what it does"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """inverts != operator to the opposite of what it does"""
        return not super().__ne__(other)
