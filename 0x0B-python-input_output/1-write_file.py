#!/usr/bin/python3
"""a module for writing into a file. overwrites file content"""


def write_file(filename="", text=""):
    """opens and writes into the given file"""
    with open(filename, "w", encoding="utf-8") as file:
        """returns the number of text written into the file"""
        return (file.write(text))
