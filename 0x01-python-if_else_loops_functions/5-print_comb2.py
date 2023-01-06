#!/usr/bin/python3
for i in range(100):
    if i < 10:
        i = str(i).zfill(2)
    print("{}".format(i), end='')
    if i != 99:
        print(", ", end='')
