#!/usr/bin/python3
"""Test suite for the Rectangle class."""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Tests the functionality of the derived class of the Base class, Rectangle."""

    def test_rectangle_w_h(self):
        """Test case for initializing width and height attributes."""
        r1_obj = Rectangle(1, 2)
        self.assertEqual(r1_obj.width, 1)
        self.assertEqual(r1_obj.height, 2)

    def test_x_cordinates(self):
        """Test case for initializing x coordinate."""
        r1_obj = Rectangle(1, 2, 3)
        self.assertEqual(r1_obj.x, 3)

    def test_y_cordinates(self):
        """Test case for initializing y coordinate."""
        r1_obj = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1_obj.y, 4)

    def test_width_validation(self):
        """Test case for validating width attribute."""
        with self.assertRaises(TypeError):
            r1_obj = Rectangle("1", 2)
        with self.assertRaises(ValueError):
            r1_obj = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r1_obj = Rectangle(0, 2)

    def test_height_validation(self):
        """Test case for validating height attribute value."""
        with self.assertRaises(TypeError):
            r1_obj = Rectangle(1, "2")
        with self.assertRaises(ValueError):
            r1_obj = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r1_obj = Rectangle(10, 0)

    def test_x_validation(self):
        """Test case for validating x coordinate value."""
        with self.assertRaises(TypeError):
            r1_obj = Rectangle(1, 3, "2")
        with self.assertRaises(ValueError):
            r1_obj = Rectangle(1, 3, -1)

    def test_y_validation(self):
        """Test case for validating y coordinate value."""
        with self.assertRaises(TypeError):
            r1_obj = Rectangle(1, 3, 4, "2")
        with self.assertRaises(ValueError):
            r1_obj = Rectangle(1, 3, 4, -2)

    def test_complete_args(self):
        """Test case for initializing all attributes including ID."""
        r1_obj = Rectangle(2, 3, 4, 5, 8)
        self.assertEqual(r1_obj.id, 8)

    def test_area_method(self):
        r1_obj = Rectangle(2, 1)
        self.assertTrue(hasattr(r1_obj, 'area'))
