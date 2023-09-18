import unittest
from models.rectangle import Rectangle
import json
import pep8


class TestRectangleClass(unittest.TestCase):

    @classmethod
    def setUp(self):
        Base._Base__nb_objects = 0

    @classmethod
    def tearDownClass(self):
        pass



if __name__ == "__main__":
    unittest.main()
