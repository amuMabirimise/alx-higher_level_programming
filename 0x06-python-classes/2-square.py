#!/usr/bin/python3
"""creating module square"""


class Square:
    """creating square classs
        with conditional statements"""
    def __init__(self, size=0):
        """initialization"""
        if type(size) is not int:
            raise TypeError("size must be an intger")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size__ = size
