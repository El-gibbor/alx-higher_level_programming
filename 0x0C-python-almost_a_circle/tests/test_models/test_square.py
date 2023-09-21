#!/usr/bin/python3
"""Test suit for the square class"""
import os
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square

class TestSquare(TestCase):
    """ Testing the Square class and its methods"""

    def test_square(self):
        """Test the area() method of the Square class"""
        sq = Square(5)
        self.assertEqual(sq.area(), 25)

    def test_square_create(self):
        """ Test creating Square instances from dictionaries"""
        with self.subTest():
            sq = Square.create(**{'id': 33})
            self.assertIsInstance(sq, Square)
            self.assertEqual(sq.id, 33)

        with self.subTest():
            sq = Square.create(**{'id': 89, 'size': 1})
            self.assertEqual(sq.size, 1)

        with self.subTest():
            sq = Square.create(**{'id': 89, 'size': 1, 'x': 11})
            self.assertEqual(sq.x, 11)

        with self.subTest():
            sq = Square.create(**{'id': 89, 'size': 1, 'x': 11, 'y': 44})
            self.assertEqual(sq.y, 44)

    def test_square_save_to_file(self):
        """ Test saving Square instances to a JSON file"""
        with self.subTest():
            Square.save_to_file(None)
            with open("Square.json", "r") as file:
                self.assertEqual(file.read(), '[]')

        with self.subTest():
            Square.save_to_file([Square(1)])
            with open("Square.json", "r") as file:
                self.assertEqual(file.read(), '[{"id": 33, "size": 1, "x": 0, "y": 0}]')

        with self.subTest():
            Square.save_to_file([])
            with open("Square.json", "r") as file:
                self.assertEqual(file.read(), '[]')

    def test_load_from_file(self):
        """Test loading from a non-existent file"""
        try:
            os.remove("Square.json")
        except:
            pass
        r1 = Square(5, 0, 0, 3)
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    def test_load_from_file_file_exists(self):
        """Test loading from an existing file"""

        # Create a Square instance, save it to a JSON file, and load it
        r1 = Square(5, 0, 0, 3)
        Square.save_to_file([r1])
        instances = Square.load_from_file()

        # Assert that the loaded instance matches the original instance
        self.assertEqual(len(instances), 1)
        self.assertEqual(instances[0].id, r1.id)


    def test_update_args(self):
        """ tests for correct update of attr values based on the passed args"""
        with self.subTest():
            r1_obj = Square(2)
            r1_obj.update(90)
            self.assertEqual(r1_obj.id, 90)

        with self.subTest():
            """tests for correct assigning of width argument"""
            r1_obj.update(90, 99)
            self.assertEqual(r1_obj.width, 99)

        with self.subTest():
            """tests for correct assigning of height argument"""
            r1_obj.update(90, 33, 99)
            self.assertEqual(r1_obj.height, 33)

        with self.subTest():
            """tests for correct assigning of x argument"""
            r1_obj.update(90, 33, 99, 44)
            self.assertEqual(r1_obj.x, 99)

        with self.subTest():
            """tests for correct attr assinging (argument for y)"""
            r1_obj.update(90, 33, 99, 44, 55)
            self.assertEqual(r1_obj.y, 44)

    def update_kwargs_square(self):
        """tests update() method with key-word arguments (id obj attr)"""
        with self.subTest():
            r1_obj = Square(2)
            r1_obj.update(**{'id': 99})
            self.assertEqual(r1_obj.id, 99)

        with self.subTest():
            """tests update() method with key-word arguments (width obj attr)"""
            r1_obj = Square(2)
            r1_obj.update(**{'id': 99, 'width': 2})
            self.assertEqual(r1_obj.width, 2)

        with self.subTest():
            """tests update() method with key-word arguments (height obj attr)"""
            r1_obj = Square(2)
            r1_obj.update(**{'id': 99, 'width': 2, 'height': 6})
            self.assertEqual(r1_obj.height, 6)

        with self.subTest():
            """tests update() method with key-word arguments (x obj attr)"""
            r1_obj = Square(2)
            r1_obj.update(**{'id': 99, 'width': 2, 'height': 6, 'x': 22})
            self.assertEqual(r1_obj.x, 22)

        with self.subTest():
            """tests update() method with key-word arguments (y obj attr)"""
            r1_obj = Square(2)
            r1_obj.update(**{'id': 99, 'width': 2, 'height': 6, 'x': 22, 'y': 4})
            self.assertEqual(r1_obj.y, 4)

