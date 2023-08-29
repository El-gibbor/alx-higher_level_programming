#!/usr/bin/python3
import sys
"""executes a func and prints exception erros to stderr"""


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as tb_error:
        print('Exception:', tb_error, file=sys.stderr)
        return None
