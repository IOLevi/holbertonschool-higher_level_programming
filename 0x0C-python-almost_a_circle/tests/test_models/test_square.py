#!/usr/bin/python3
"""Unittest for Square"""


import unittest
from models.square import Square
import sys
from io import StringIO


class TestSquare(unittest.TestCase):
    """unittest for Square"""

    def setUp(self):
        'nothing'
        pass

    def test_square_init(self):
        "test 1"
        f = Square(5)
        self.assertEqual(f.size, 5)
        self.assertEqual(f.area(), 25)
        f.size = 6
        self.assertEqual(f.area(), 36)
        f.id = 1
        self.assertEqual(str(f), "[Square] (1) 0/0 - 6")
        f.height = 12
        self.assertEqual(f.size, 12)

        with self.assertRaises(ValueError):
            f.size = -1
            f.size = 0

    def test_square_update(self):
        "test 2"
        f = Square(5)
        f.update(4)
        self.assertEqual(f.id, 4)

        f.update(size=4)
        self.assertEqual(f.size, 4)

        f.update(3, 4, 5, 6)
        self.assertEqual(str(f), "[Square] (3) 5/6 - 4")

        f.update(4, x=44)
        self.assertEqual(str(f), "[Square] (4) 5/6 - 4")

    def test_to_dict(self):
        "test 3"
        f = Square(5)
        b = {'id': 1, 'size': 5, 'x': 0, 'y': 0}
        self.assertEqual(set(f.to_dictionary()), set(b))

    def test_display(self):
        "test 5.5"
        r1 = Square(1)
        output = StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#\n")
        output.close()

    def test_displayxy(self):
        "test 5.6"
        r1 = Square(1)
        r1.x = 1
        r1.y = 1
        output = StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n #\n")
        output.close()


if __name__ == "__main__":
    unittest.main()
