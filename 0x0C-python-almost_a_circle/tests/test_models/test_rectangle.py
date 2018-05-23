#!/usr/bin/python3
"""Unittest for Rectangle"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """unittest for Rectangle"""

    def setUp(self):
        "set up"
        self.r1 = Rectangle(1, 1, id=12)

    def test_id(self):
        "test 1"
        Base._Base__nb_objects = 0
        self.assertEqual(self.r1.id, 12)

    def test_getters(self):
        "test 2"
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 1)

    def test_setters(self):
        "test 3"
        self.r1.width = 3
        self.assertEqual(self.r1.width, 3)

    def test_validation(self):
        "test 4"
        with (self.assertRaises(TypeError)):
            self.r1.width = 1.4
            self.r1.height = "hello"

    def test_validation2(self):
        "test 4"
        with (self.assertRaises(ValueError)):
            self.r1.height = 0
            self.r1.width = -1

    def test_area(self):
        "test 5"
        self.assertEqual(self.r1.area(), 1)
        r2 = Rectangle(4, 4)
        self.assertEqual(r2.area(), 16)

    # def test_display(self):
    #     self.assertEqual(self.r1.display(), "#")
    # not sure how to test this other than using
    # in module pytest

    def test_str_overload(self):
        "test 6"
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    # def test_display_xy(self):

    def test_update_function(self):
        "test 7"
        r2 = Rectangle(10, 10, 10, 10)

        r2.update(89)
        self.assertEqual(str(r2), "[Rectangle] (89) 10/10 - 10/10")
        r2.update(89, 2)
        self.assertEqual(str(r2), "[Rectangle] (89) 10/10 - 2/10")
        r2.update(89, 2, 3)
        self.assertEqual(str(r2), "[Rectangle] (89) 10/10 - 2/3")
        r2.update(89, 2, 3, 4)
        self.assertEqual(str(r2), "[Rectangle] (89) 4/10 - 2/3")
        r2.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r2), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        "test 8"
        r2 = Rectangle(10, 10, 10, 10)
        r2.update(89)
        r2.update(height=1)
        self.assertEqual(str(r2), "[Rectangle] (89) 10/10 - 10/1")
        r2.update(2, height=12)
        self.assertEqual(str(r2), "[Rectangle] (2) 10/10 - 10/1")

    def test_to_dict(self):
        "test 9"
        f = Rectangle(1, 1, 1, 1, 1)
        b = {'height': 1, 'id': 1, 'width': 1, 'x': 1, 'y': 1}
        self.assertEqual(set(f.to_dictionary()), set(b))
        f.update(id=9)
        b = {'height': 1, 'id': 9, 'width': 1, 'x': 1, 'y': 1}
        self.assertEqual(set(f.to_dictionary()), set(b))

    def test_to_json_string(self):
        "test 10"
        f = Rectangle(1, 1, 1, 1, 1)
        a = [f.to_dictionary()]
        a = Rectangle.to_json_string(a)
        self.assertEqual(type(a), str)


if __name__ == "__main__":
    unittest.main()
