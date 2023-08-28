#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for elem in range(x):
        try:
            print(my_list[elem], end='')
        except IndexError:
            pass
        else:
            elem += 1
    print()
    return elem
