#!/usr/bin/python3
"""Unittest for base """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """unittest for Base"""

    def setUp(self):
        'set up'
        self.b1 = Base()

    def test_init_id(self):
        "test1"
        self.assertEqual(self.b1.id, 1)
        Base.__nb_objects = 0
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_init_id_val(self):
        'test 2'
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_to_json_string(self):
        "test 3"
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)


if __name__ == "__main__":
    unittest.main()
