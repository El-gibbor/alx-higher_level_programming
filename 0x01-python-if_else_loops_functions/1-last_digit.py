#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
value = number % 10
if value > 5:
    print(f"Last digit of {number:d} is {value:d} and is greater than 5")
elif value == 0:
    print(f"Last digit of {number:d} is {value:d} and is zero")
elif value < 6:
    print(f"Last digit of {number:d} is {value:d} and less than 6 and not 0")
