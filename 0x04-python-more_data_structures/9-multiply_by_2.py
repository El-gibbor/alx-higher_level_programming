#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dict_by_2 = {}
    for k, v in a_dictionary.items():
        dict_by_2[k] = v * 2
    return dict_by_2
