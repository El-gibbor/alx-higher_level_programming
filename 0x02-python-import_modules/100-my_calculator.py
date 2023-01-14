#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import *

while len(sys.argv) < 4:
    print("usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3]

if operator == "+":
    sum = add(a, b)
elif operator == "-":
    sum = sub(a, b)
elif operator == "*":
    sum = mul(a, b)
elif operator == "/":
    sum = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

print("{} {} {} = {}".format(a, operator, b))
