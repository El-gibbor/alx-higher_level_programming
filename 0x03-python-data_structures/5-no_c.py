#!/usr/bin/python3

def no_c(my_string):
    no_c_str = ''.join([i for i in my_string if i != 'c' and i != 'C'])
    return no_c_str
