#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value), end="")
        return True
    """handles the error of str type parsed to int format"""
    except ValueError:
        return False
