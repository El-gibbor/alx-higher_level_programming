#!/usr/bin/python3
import sys
"""prints an int and redirects exception errors to stderr"""


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value), end='\n')
        return True
    except Exception as tb_error:
        print('Exception:', tb_error, file=sys.stderr)
        return False
