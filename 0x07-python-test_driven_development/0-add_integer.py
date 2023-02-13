#!/usr/bin/python3
"""a module for addition"""


def add_integer(a, b=98):
    """returne the sum of two integers

    Args:
        a (int/float): first paremeter
        b (int, float): second paremeter. Defaults to 98.

    Raises:
        TypeError: if a and b are either not int or float
        
    Returns:
        (int): the sum of paremeter a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)