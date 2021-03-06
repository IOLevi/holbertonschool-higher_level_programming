#!/usr/bin/python3
"""Unittest for Rectangle"""


import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys


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

    def test_display(self):
        "test 5.5"
        output = StringIO()
        sys.stdout = output
        self.r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#\n")
        output.close()

    def test_displayxy(self):
        "test 5.6"
        self.r1.x = 1
        self.r1.y = 1
        output = StringIO()
        sys.stdout = output
        self.r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n #\n")
        output.close()

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
    
    def test_checkers_1(self):
        "test 11"
        Base._Base__nb_objects = 0
        a = Rectangle(1, 2)
        self.assertEqual(str(a), "[Rectangle] (8) 0/0 - 1/2")
        
        b = Rectangle(1, 2, 3)
        self.assertEqual(str(b), "[Rectangle] (9) 3/0 - 1/2")

        c = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(c), "[Rectangle] (10) 3/4 - 1/2")

        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, 0)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
        
        
        
        # e = Rectangle(1, "2")
        # self.assertEqual()

        # f = Rectangle(1, 2, "3")
        # self.assertEqual()

        # g = Rectangle(1, 2, 3, "4")
        # self.assertEqual()

        # h = Rectangle(-1, 2)
        # self.assertEqual()

        # i = Rectangle(1, -2)
        # self.assertEqual()

        # j = Rectangle(0, 2)
        # self.assertEqual()

        # k = Rectangle(1, 0)
        # self.assertEqual()

        # l = Rectangle(1, 2, -3)
        # self.assertEqual()

        # m = Rectangle(1, 2, 3, -4)
        # self.assertEqual()






if __name__ == "__main__":
    unittest.main()
