#!/usr/bin/python3
"""module for printing name"""


def say_my_name(first_name, last_name=""):
    """defines a function that prints name

    Args:
        first_name (str): first name
        last_name (str, optional): last name Defaults to "".

    Raises:
        TypeError: if first name is not a string
        TypeError: if last name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))