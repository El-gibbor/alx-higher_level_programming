#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    r2.update(**{ 'id': 89 })
    print(r2)
    list_rectangles_input = [r1, r2]

    # print(callable(r1.area()))
    # print(dir(r1))