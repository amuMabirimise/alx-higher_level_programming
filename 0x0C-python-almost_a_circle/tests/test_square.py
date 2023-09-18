import unittest
from models.square import Square
import json
import pep8


class TestSquareClass(unittest.TestCase):

    @classmethod
    def setUp(self):
        Base._Base__nb_objects = 0

    @classmethod
    def tearDownClass(self):
        pass

    # Add your Square class specific tests here


if __name__ == "__main__":
    unittest.main()
