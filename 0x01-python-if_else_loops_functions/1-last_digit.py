#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
int_str = str(number)
lastValue = int(int_str[-1])
if number < 0 and lastValue != 0:
    print("Last digit of {} is -{} and is less than 6 and not 0")

