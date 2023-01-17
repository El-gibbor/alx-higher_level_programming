#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # iterate throu the keys and values (k for keys, v for the values)
    for k, v in sorted(a_dictionary.items()):
        # print both keys and values in sorted order
        print("{}: {}".format(k, v))
