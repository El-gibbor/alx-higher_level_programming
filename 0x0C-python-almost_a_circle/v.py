#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([Square(5)])

    with open("Rectangle.json", "r") as file:
        print(file.read())