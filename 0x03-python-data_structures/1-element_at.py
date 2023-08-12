#!/usr/bin/python3
""" Retrieves an element from a list """


def element_at(my_list, idx):
    return None if idx < 0 or idx > len(my_list) else my_list[idx]
