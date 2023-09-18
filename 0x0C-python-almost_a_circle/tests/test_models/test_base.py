#!/usr/bin/python3
"""a Test suit module for the base class"""
from models.base import Base
import unittest


# class Test_base(unittest.TestCase):
#     """
#     Tests for the automatic assigning of Ids to all base instance.
#         - Assigning id automatically.
#         - Id increases by at new instantiation after the prev one
#         - Makes use of user provided Id instead of automatic assigning
#     """

#     def setUp(self):
#         """ test env setup and instantiation of base objs """
#         self.base_obj = Base()
#         self.base_obj_1 = Base()
#         self.base_obj_2 = Base(99)
#         self.base_obj_3 = Base("str")
#         self.base_obj_4 = Base([2, 2, 3])

#     def tearDown(self):
#         """Test cleanup - delete instance after each test"""
#         del self.base_obj
#         del self.base_obj_1
#         del self.base_obj_2
#         del self.base_obj_3
#         del self.base_obj_4

#     def test_base_id(self):
#         """ Correct Id assignment of all base instance """
#         self.assertEqual(self.base_obj.id, 1)
#         self.assertEqual(self.base_obj_1.id, 2)
#         self.assertEqual(self.base_obj_2.id, 99)
#         self.assertEqual(self.base_obj_3.id, "str")
#         self.assertEqual(self.base_obj_4.id, [2, 2, 3])

class TestBase(unittest.TestCase):
    """
    Tests for the Base class.
    """

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
        base_obj = Base("str")
        self.assertEqual(base_obj.id, "str")

    def test_non_integer_id_list(self):
        """Test when a non-integer ID (list) is provided."""
        base_obj = Base([2, 2, 3])
        self.assertEqual(base_obj.id, [2, 2, 3])
