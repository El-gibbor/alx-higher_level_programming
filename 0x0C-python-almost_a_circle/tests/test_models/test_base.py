#!/usr/bin/python
"""This is a unnitest module containing all posible test cases
for all the methods inside Base.py modsule
"""
from unittest import TestCase, main
from models.base import Base


class TestBase(TestCase):
    """defines various crucial test case methods"""

    def setUp(self):
        self.base1 = Base()
        self.base2 = Base()

    def test_id_initializing(self):
        self.assertLess(self.base1.id, self.base2.id)


if __name__ == "__main__":
    main()
