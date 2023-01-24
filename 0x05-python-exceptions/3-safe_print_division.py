#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        division = a / b
        # handles error & return None if valued is beign divided by 0
    except ZeroDivisionError:
        division = None
    finally:
        # finally outputs all (error value -> None & the divisible values
        print("Inside result: {}".format(division))
    return (division)
