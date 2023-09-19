#!/usr/bin/python3
""" holds a module that appends test to a file"""


def append_write(filename="", text=""):

    """ appends a string at the end of a text file """
    with open(filename, 'a') as a_file:
        return (a_file.write(text))
