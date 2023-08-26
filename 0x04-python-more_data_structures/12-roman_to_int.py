#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_figures = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    result, prev_value = 0, 0

    for char in reversed(roman_string):
        value = roman_figures[char]
        if value >= prev_value:
            result += value
        else:
            result -= value
        prev_value = value  # holds L12 at each iteration after validating L13
    return result
