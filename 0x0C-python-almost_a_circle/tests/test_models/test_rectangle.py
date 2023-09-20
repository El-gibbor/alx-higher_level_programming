#!/usr/bin/python3
"""Test suite for the Rectangle class."""
import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(TestCase):
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
        """tests for the existence of this method() in the class"""
        r1_obj = Rectangle(2, 1)
        self.assertTrue(hasattr(r1_obj, 'area'))
        self.assertTrue(callable(r1_obj.area))

    def test_str_method(self):
        """test for the existence of __str__()"""
        r1_obj = Rectangle(2, 1)
        self.assertTrue(hasattr(r1_obj, '__str__'))

    def test_display(self):
        """tests the existence of this method() in the class instance"""
        r1_obj = Rectangle(2, 2)
        self.assertTrue(r1_obj.display, True)
        self.assertTrue(callable(r1_obj.display))

    def test_display_stdout(self):
        """ tests for correct character display to stdout (without x & y)"""
        with self.subTest():
            r1_obj = Rectangle(2, 2)
            with patch('sys.stdout', new=StringIO()) as to_stdout:
                r1_obj.display()
                self.assertEqual(to_stdout.getvalue(), '##\n##\n')

        with self.subTest():
            """ tests for correct character display to stdout (without y)"""
            r1_obj = Rectangle(2, 2, 2)
            with patch('sys.stdout', new=StringIO()) as to_stdout:
                r1_obj.display()
                self.assertEqual(to_stdout.getvalue(), '  ##\n  ##\n')