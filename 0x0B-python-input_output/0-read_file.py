#!/usr/bin/python3
""" a module with a function that reads a text file """


def read_file(filename=''):
    """ reads a file content """
    with open(filename) as file_content:
        print(file_content.read())
