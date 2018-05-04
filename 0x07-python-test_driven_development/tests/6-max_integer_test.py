#!/usr/bin/python3
"""Unittest for max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest for max_integer"""
    def setUp(self):
        pass
    def test_default_1(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_default_2(self):
        self.assertEqual(max_integer([1,3,4,2]), 4)
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    #assertEqual
    #assertItemEqual (sorted sorted)
    #assertLess
    #assertLessEqual
    #assertGreaterEqual
    #assertGreater
    #assertRaises(SomeException)
    #assertIsInstance
    #assertIsNone (NotNone)
    #assertIn
if __name__ == "__main__":
    unittest.main()
