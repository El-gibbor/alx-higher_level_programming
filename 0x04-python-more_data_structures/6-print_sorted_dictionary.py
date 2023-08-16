#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    [print(k, v) for k, v in sorted(a_dictionary.items())]  # dict comprehesion
