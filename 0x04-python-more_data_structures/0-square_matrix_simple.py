#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = [[sqr * sqr for sqr in sublist] for sublist in matrix]
    return result
