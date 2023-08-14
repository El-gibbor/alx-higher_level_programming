#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for outer_list in matrix:
        for idx, sub_list in enumerate(outer_list):
            if idx < 2:
                print('{}'.format(sub_list), end=' ')
            else:
                print('{}'.format(sub_list), end='')
        print()
