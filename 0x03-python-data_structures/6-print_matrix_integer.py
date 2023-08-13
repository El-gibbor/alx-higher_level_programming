#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) < 1:
            return None 
    for outer_list in matrix:
        for sub_list in outer_list:
            print('{}'.format(sub_list), end='')
        print()
