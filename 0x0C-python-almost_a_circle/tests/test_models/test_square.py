#!/usr/bin/python3
"""Test suit for the square class"""
from models.square import Square
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

class TestSquare(TestCase):
    """ Testing the square class and its methods()"""

    def test_square(self):
        sq = Square(5)
        self.assertEqual(sq.area(), 25)

    def test_square_create(self):
        with self.subTest():
            sq = Square.create(**{'id': 33})
            self.assertIsInstance(sq, Square)
            self.assertEqual(sq.id, 33)

        with self.subTest():
            sq = Square.create(**{ 'id': 89, 'size': 1 })
            self.assertEqual(sq.size, 1)

        with self.subTest():
            sq = Square.create(**{ 'id': 89, 'size': 1, 'x': 11})
            self.assertEqual(sq.x, 11)

        with self.subTest():
            sq = Square.create(**{ 'id': 89, 'size': 1, 'x': 11, 'y': 44})
            self.assertEqual(sq.y, 44)

    def test_square_save_to_file(self):
        with self.subTest():
            Square.save_to_file(None)
            with open("Square.json", "r") as file:
                self.assertEqual(file.read(), '[]')

        with self.subTest():
            Square.save_to_file([Square(1)])
            with open("Square.json", "r") as file:
                self.assertEqual(file.read(), '[{"id": 32, "size": 1, "x": 0, "y": 0}]')
