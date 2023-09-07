#!/usr/bin/python3
""" Addition Module"""


def add_integer(a, b=98):
    """Add two numbers int or float
    raise errors where expected
    return a + b
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
