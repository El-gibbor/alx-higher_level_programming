#!/usr/bin/python3
for i in range(122, 96, -1):
    alternated_char = i - 32 if (i % 2) else i
    print(chr(alternated_char), end='')
