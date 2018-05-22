#!/usr/bin/python3
"""Unittest for base """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """unittest for Base"""

    def setUp(self):
        self.b1 = Base()

    def test_init_id(self):
        self.assertEqual(self.b1.id, 1)
        Base.__nb_objects = 0
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_init_id_val(self):
        b2 = Base(12)
        self.assertEqual(b2.id, 12)


if __name__ == "__main__":
    unittest.main()
