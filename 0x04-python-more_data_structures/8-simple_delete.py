#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # remove key-value pair or return defualt(None) if it doesnt exit.
    a_dictionary.pop(key, None) 
    return a_dictionary
