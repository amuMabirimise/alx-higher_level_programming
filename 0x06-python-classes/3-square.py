#!/usr/bin/python3
""" Module """


class Square:
    """ Square class create """
    def __init__(self, size=0):
        """
        initialize square"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
            set square square area"""

        return self.__size ** 2
