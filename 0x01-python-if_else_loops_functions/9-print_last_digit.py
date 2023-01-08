#!/usr/bin/python3
def print_last_digit(number):
        if number <= 0 or number > 0:
            new_val = str(number)
            print(new_val[-1:], end='')
            return new_val[-1:]
