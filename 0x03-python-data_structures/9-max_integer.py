#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    my_max = my_list[0]
    for i in my_list:
        if i > my_max:
            my_max = i
    return my_max
