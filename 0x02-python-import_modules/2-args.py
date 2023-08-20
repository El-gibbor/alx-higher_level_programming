#!/usr/bin/python3

from sys import argv

if (len(argv) - 1) == 0:
    print('0 arguments')
elif (len(argv) - 1) == 1:
    [print(f'1 argument:\n{i}: {j}') for i, j in enumerate(argv[1:], 1)]
else:
    print('{} arguments'.format(len(argv) - 1))
    for i, arg in enumerate(argv[1:], 1):
       print('{}: {}'.format(i, arg))