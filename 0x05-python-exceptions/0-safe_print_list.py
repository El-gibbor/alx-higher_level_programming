#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for nb_print in range(x):
        try:
            print(my_list[nb_print])
        except IndexError:
            pass
        else:
            nb_print += 1
    return nb_print
