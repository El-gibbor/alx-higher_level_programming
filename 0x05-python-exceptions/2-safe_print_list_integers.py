#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    for i in my_list[:x]:
        print(my_list[i])

my_list = [1, 2, 3, 4, 5]
safe_print_list_integers(my_list, 2)