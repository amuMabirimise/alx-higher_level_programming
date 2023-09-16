#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)  # Call the super class with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Width must be a positive integer.")
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Height must be a positive integer.")
        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise ValueError("X must be an integer.")
        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise ValueError("Y must be an integer.")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        for i in range(self.height):
            print('#' * self.width)

    def __str__(self):
        return (
        f"[Rectangle] ({self.id}) {self.x}/{self.y} - " +
        f"{self.width}/{self.height}"
    )

    def update(self, *args):
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

    def update(self, *args, **kwargs):
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
