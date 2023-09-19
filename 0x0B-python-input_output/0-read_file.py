#!/usr/bin/python3
""" A script containing a function that reads a file"""


def read_file(filename=""):
    """ a function that reads a text file (UTF8) and prints it to stdout:
    Args:
        filename(str): file path
    """
    with open(filename) as read_file:
        content = read_file.read()
        print(content, end="")
