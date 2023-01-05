#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def lastValue():
    int_str = str(number)
    lastValue = int(int_str[-1])
    return -lastValue if (number < 0) else lastValue


print(f"Last digit of {number:d} is {lastValue():d} and is", end=' ')
if lastValue() > 5:
    print("is greater than 5")
elif lastValue() < 6 != 0:
    print("less than 6 and not 0")
else:
    print("and is 0")
