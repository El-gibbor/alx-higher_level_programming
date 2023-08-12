#!/usr/bin/python3

def element_at(my_list, idx):
    return None if idx < 0 or idx > (len(my_list) - 1) else my_list[idx]
