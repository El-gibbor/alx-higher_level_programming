#!/usr/bin/python3
""" this module contains a func that writes a str to a text file (UTF8)"""


def write_file(filename="", text=""):
    """ writes a str to a txt file """

    with open(filename, 'w') as txt_f:
        return txt_f.write(text)
