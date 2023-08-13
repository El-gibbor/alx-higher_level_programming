#!/usr/bin/python3

def no_c(my_string):
    new_str = ''.join([i for i in my_string if i != 'c' and i != 'C'])
    return new_str
