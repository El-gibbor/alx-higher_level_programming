#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sqr_matrix = [[num ** 2 for num in i] for i in matrix]
    return sqr_matrix
