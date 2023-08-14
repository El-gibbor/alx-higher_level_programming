#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_num = my_list[0]
    for num in my_list:
        if num > max_num:
            max_num = num
    return
