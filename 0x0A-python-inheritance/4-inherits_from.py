#!/usr/bin/python3
"""True if obj is an instance of the class "a_class" or if obj is an instance
    of a class that inherited from a_class, otherwise it should return False.
"""


def inherits_from(obj, a_class):
    """checks for the above documented conditions"""

    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
