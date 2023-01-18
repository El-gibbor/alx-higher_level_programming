#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # using list comprehension, iterate through dict $ mul the values in keys
    return {k: v * 2 for k, v in a_dictionary.items()}
