#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        sys.stderr.write("Exception: {}\n".format(sys.exc_info()[1]))
        return False
