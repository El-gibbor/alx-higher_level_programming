#!/usr/bin/python3
"""a Test suit module for the base class"""
# from models.base import Base
# from unittest import TestCase


# class Test_base(TestCase):
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

#     def tearDown(self) -> None:
#         """Test cleanup - delete instance after each test"""
#         del self.base_obj
#         del self.base_obj_1
#         del self.base_obj_2

#     def test_base_id(self):
#         """ Correct Id assignment of all base instance """
#         self.assertEqual(self.base_obj.id, 1)
#         self.assertEqual(self.base_obj_1.id, 2)
#         self.assertEqual(self.base_obj_2.id, 99)
#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import json
import inspect

'''
    Creating test cases for the base module
'''


class test_base(unittest.TestCase):
    '''
        Testing base
    '''
    def test_id_none(self):
        '''
            Sending no id
        '''
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        '''
            Sending a valid id
        '''
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_id_zero(self):
        '''
            Sending an id 0
        '''
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        '''
            Sending a negative id
        '''
        b = Base(-20)
        self.assertEqual(-20, b.id)

    def test_id_string(self):
        '''
            Sending an id that is not an int
        '''
        b = Base("Betty")
        self.assertEqual("Betty", b.id)

    def test_id_list(self):
        '''
            Sending an id that is not an int
        '''
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        '''
            Sending an id that is not an int
        '''
        b = Base({"id": 109})
        self.assertEqual({"id": 109}, b.id)

    def test_id_tuple(self):
        '''
            Sending an id that is not an int
        '''
        b = Base((8,))
        self.assertEqual((8,), b.id)

    def test_to_json_type(self):
        '''
            Testing the json string
        '''
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")
