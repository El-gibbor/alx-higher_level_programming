#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # iterate through the keys and its value (k for keys, v for the values)
    for k, v in sorted(a_dictionary.items()):
        # print both keys and values/items in sorted order
        print("{}: {}".format(k, v))
