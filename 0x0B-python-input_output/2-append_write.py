#!/usr/bin/python3
def append_write(filename="", text=""):
    """ appends a string at the end of a text file """
    with open(filename, 'a') as a_file:
        return (a_file.write(text))
