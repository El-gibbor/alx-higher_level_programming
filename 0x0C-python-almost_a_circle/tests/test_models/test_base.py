#!/usr/bin/python3
"""a Test suit module for the base class"""
from models.base import Base
from unittest import TestCase

class TestBase(TestCase):

    def setUp(self):
        """Set up for each test case in this class."""
        Base.__nb_objects = 0  # Reset the ID count before each test

    def test_auto_increment_id(self):
        """Test that IDs are assigned automatically and increase."""
        base_obj_1 = Base()
        base_obj_2 = Base()
        self.assertEqual(base_obj_1.id, 1)
        self.assertEqual(base_obj_2.id, 2)

    def test_user_provided_id(self):
        """Test when the user provides an ID."""
        base_obj = Base(99)
        self.assertEqual(base_obj.id, 99)

    def test_non_integer_id(self):
        """Test when a non-integer ID is provided."""
        with self.subTest():
            base_obj = Base("str")
            self.assertEqual(base_obj.id, "str")

        with self.subTest():
            base_obj = Base([2, 2, 3])
            self.assertEqual(base_obj.id, [2, 2, 3])

    def test_to_json_str(self):
        """Tests for the correct behavior of to_json_string() method"""
        base_obj = Base()
        self.assertEqual(base_obj.to_json_string(None), '[]')
        self.assertEqual(base_obj.to_json_string([]), '[]')
        self.assertEqual(base_obj.to_json_string([{"id": 2}]), '[{"id": 2}]')

    def test_from_json_str(self):
        """Tests for correct expected behavior of this method()"""
        base_obj = Base()
        self.assertEqual(base_obj.from_json_string(None), [])
        self.assertEqual(base_obj.from_json_string('[]'), [])
        self.assertEqual(base_obj.from_json_string('[{"id": 2}]'), [{"id": 2}])
        with self.assertRaises(TypeError):
            Base.from_json_string(99)
