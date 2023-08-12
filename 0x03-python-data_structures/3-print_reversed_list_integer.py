#!/usr/bin/python3
"""  prints all integers of a list, in reverse order. """

def print_reversed_list_integer(my_list=[]):
    if type(my_list) is list:
        for num in my_list[::-1]:
            print("{:d}".format(num))
