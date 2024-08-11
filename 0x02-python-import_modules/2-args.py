#!/usr/bin/python3
import sys

argv_len = len(sys.argv) -1

# args_var = 'arguments:' if argv_len > 1 else args_var = 'argument.'
if argv_len == 1:
    print('0 arguments.')
elif argv_len == 2:
        print(f'1 argument:\n1: {sys.argv[1]}')
else:
    print(f'{argv_len} arguments:')
    for i, index in enumerate(range(1, len(sys.argv)), start=1):
        print(f'{index}: {sys.argv[i]}')
