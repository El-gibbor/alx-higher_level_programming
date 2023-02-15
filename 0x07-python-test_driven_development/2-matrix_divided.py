#!/usr/bin/python3
"""a module that carries out division operation on all
elements of a matrix
"""
import math


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:
        matrix (list(int/float)): lists of int or floats to be divided
        div (int/float): the divisor

    Raises:
        TypeError: matrix is not list of lists of int/floats.
        TypeError: if each row of the matrix is not of the same size.
        TypeError: if divisor is not an integer or float.
        ZeroDivisionError: if devisor is equal to zero (0)

    Returns:
        list of lists: new matrix (divided elements)
    """
    for rows in matrix:
        for columns in rows:
            if not isinstance(columns, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrixx = []
    for r in matrix:
        new_row = []
        for columxx in r:
            new_row.append(round(columxx/div, 2))
        matrixx.append(new_row)
    return matrixx