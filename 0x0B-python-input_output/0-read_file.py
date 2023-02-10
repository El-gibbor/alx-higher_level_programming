#!/usr/bin/python3
"""a module for file reading"""


def read_file(filename=""):
    """opens the parsed file in default read mode"""
    with open(filename, encoding="utf-8") as file:
        """prints file content with read method"""
        print(file.read())
