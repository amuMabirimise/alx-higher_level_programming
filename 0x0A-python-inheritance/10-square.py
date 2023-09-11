#!/usr/bin/python3
"""Class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from Retangle"""
    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        self.integer_validator('size', self.__size)

    def area(self):
        """area of square"""
        return self.__size * self.__size

    def __str__(self):
        """__str__"""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
