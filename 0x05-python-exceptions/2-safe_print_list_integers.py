#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elements = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elements += 1
            # indexError is not handled. an error will be raised
        except (ValueError, TypeError):
            # skips the handled error and iterate till the loop end
            continue
    print("")
    return (elements)
