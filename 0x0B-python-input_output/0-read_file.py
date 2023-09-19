#!/usr/bin/python3
""" a module with a function that reads a text file """


def read_file(filename=''):
    """ reads a file content """

    with open(filename, 'r') as file_content:
        to_stdout = file_content.read()
        print(to_stdout)
