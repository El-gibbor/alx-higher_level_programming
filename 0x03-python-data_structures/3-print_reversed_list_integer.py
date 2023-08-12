#!/usr/bin/python3
""" prints all integers of a list, in reverse order. """

def print_reversed_list_integer(my_list=[]):
    if type(my_list) is list:
        new_list = my_list[::-1]
        for num in new_list:
            print('{}'.format(num))
