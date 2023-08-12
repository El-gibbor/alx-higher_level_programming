#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if type(my_list) is list:
        for num in my_list[::-1]:
            print("{:d}".format(num))
