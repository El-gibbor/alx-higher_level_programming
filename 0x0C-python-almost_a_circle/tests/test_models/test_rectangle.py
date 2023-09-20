#!/usr/bin/python3
"""a Test suit module for the rectangle class"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Tests the functionality of the derived class of base."""

    def test_rectangle_w_h(self):
        r1_obj = Rectangle(1, 2)
        self.assertEqual(r1_obj.width, 1)
        self.assertEqual(r1_obj.height, 2)

    def test_x_cordinates(self):
        r1_obj = Rectangle(1, 2, 3)
        self.assertEqual(r1_obj.x, 3)

    def test_y_cordinates(self):
        r1_obj = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1_obj.y, 4)

    def test_width_validation(self):
        with self.assertRaises(TypeError):
            r1_obj = Rectangle("1", 2)
        with self.assertRaises(ValueError):
            r1_obj = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r1_obj = Rectangle(0, 2)

    def test_height_validation(self):
        with self.assertRaises(TypeError):
            r1_obj = Rectangle(1, "2")

