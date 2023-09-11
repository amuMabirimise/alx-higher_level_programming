#!/usr/bin/python3
"""class"""


class BaseGeometry:
    """Class with Public instance method
    that raises an Exception
    with the message
    """
    def area(self):
        raise Exception("area() is not implemented")
