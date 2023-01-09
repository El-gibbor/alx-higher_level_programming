#!/usr/bin/python3
j = 122
while j > 96:
    print("{}".format(chr(j) if j % 2 == 0 else chr(j - 32)), end='')
    j -= 1
