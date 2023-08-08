#!/usr/bin/python3
for i in range(ord('a'), ord('{')):
    if i == ord('q') or i == ord('e'):
        continue
    print(chr(i), end='')
