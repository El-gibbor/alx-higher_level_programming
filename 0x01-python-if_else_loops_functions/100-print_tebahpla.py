#!/usr/bin/python3
for i in range(122, 96, -1):
    alternated = i - 32 if (i % 2) else i
    print('{}'.format(chr(alternated)), end='')
