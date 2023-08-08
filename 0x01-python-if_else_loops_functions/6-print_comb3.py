#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if i != j or i < j:
            print('{}{}'.format(i, j), end=' ')
