#!/usr/bin/python3
"""a Test suit module for the base class"""
from models.base import Base
from unittest import TestCase


class Test_base(TestCase):
    """ Tests for the automatic assigning of Ids to all base instance."""

    def test_auto_increment_id(self):
        """Test that IDs are assigned automatically and increases."""
        base_obj_1 = Base()
        base_obj_2 = Base()
        self.assertEqual(base_obj_1.id, 1)
        self.assertEqual(base_obj_2.id, 2)

    def test_user_provided_id(self):
        """Test when the user provides an ID."""
        base_obj = Base(99)
        self.assertEqual(base_obj.id, 99)

    def test_non_integer_id(self):
        """ Test when a non-integer ID is provided."""
        with self.subTest():
            base_obj = Base("str")
            self.assertEqual(base_obj.id, "str")

        with self.subTest():
            base_obj = Base([2, 2, 3])
            self.assertEqual(base_obj.id, [2, 2, 3])

    def test_to_json_str(self):
        """Tests for the correct behaviour of to_json_string() method"""
        base_obj = Base()
        self.assertEqual(base_obj.to_json_string(None), '[]')
        self.assertEqual(base_obj.to_json_string([]), '[]')
        self.assertEqual(base_obj.to_json_string([{"id": 2}]), '[{"id": 2}]')

    def test_from_json_str(self):
        """tests for correct expected behaviuor of this method()"""
        base_obj = Base()
        self.assertEqual(base_obj.from_json_string(None), [])
        self.assertEqual(base_obj.from_json_string('[]'), [])
        self.assertEqual(base_obj.from_json_string('[{"id": 2}]'), [{"id": 2}])
