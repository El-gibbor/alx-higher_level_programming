#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        fizzBuzz = "Fizz" * (not i % 3) + "Buzz" * (not i % 5)
        if not fizzBuzz:
            fizzBuzz = i
        print('{}'.format(fizzBuzz), end=' ')
