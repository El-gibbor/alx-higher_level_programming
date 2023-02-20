#!/usr/bin/python3
def pascal_triangle(n):
    result = []
    if n <= 0:
        return result
    for i in range(n):
        row = []
        C = 1
        for j in range(i+1):
            row.append(C)
            C = C * (i - j) // (j + 1)
        result.append(row)
    return result  