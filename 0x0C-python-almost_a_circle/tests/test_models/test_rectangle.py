#!/usr/bin/python3
"""a Test suit module for the rectangle class"""
from models.base import Base
from unittest import TestCase
from models.rectangle import Rectangle


class Test_rectangle(TestCase):
    """ Tests the functionality of derived base class """

    def test_obj_instantiation(self):
        """correct behaviour of the inherited superclass constructor"""
        rect_obj = Rectangle(10, 22)
        rect_obj_1 = Rectangle(10, 232)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect_obj.id, 1)
        self.assertEqual(rect_obj_1.id, 2)
        self.assertEqual(r3.id, 12)