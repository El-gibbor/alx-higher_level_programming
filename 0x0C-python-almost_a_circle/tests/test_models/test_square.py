#!/usr/bin/python3
"""Test suit for the square class"""
from models.square import Square
from unittest import TestCase


class TestSquare(TestCase):
    """ Testing the square class and its methods()"""

    def test_square(self):
        sq = Square(5)
        self.assertEqual(sq.area(), 25)