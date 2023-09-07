#!/usr/bin/python3

#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defining unitest for max_integer()"""
    def test_ramdom_list(self):
        """ test from a list of random numbers"""
        ran = [3, 0, 7 , 9, 32]
        self.assertEqual(max_integer(ran, 32))

    def test_odered_list(self):
        """testing fro a list that is odered"""
        orded_list = [2, 4, 6, 8 ,9]
        self.assertEqual(max_integer(orded, 9))

    def test_empty_list(self):
        """ passing an empty list"""
        empty = []
        self.assertEqual(max_integer(empty,))

    def test_list_float(self):
        """passing list with float"""
        float_list = [2.1, 20.3, 3.1, 4.5]
        self.assertEqual(max_integer(float_list, 4.5))

    def test_list_string(self):
        """passing list with strings"""
        str_list = "my name is "
        with self.assertRaise(TypeError):
            max_integer(str_list)


    if __name__ == "__main__":
        unittest.main()
