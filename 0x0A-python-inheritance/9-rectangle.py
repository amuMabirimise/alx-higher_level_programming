#!/usr/bin/python3
"""class"""


class BaseGeometry:
    """Class with Public instance method
    that raises an Exception
    with the message
    """
    def area(self):
        """that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """a class that inherits from BaseGeometry
    Instantiation with width and height
    """
    def __init__(self, width, height):
        """ initalization"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """rectangle description: """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
