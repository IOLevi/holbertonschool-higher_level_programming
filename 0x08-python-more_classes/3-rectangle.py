#!/usr/bin/python3
"""rectangle module"""


class Rectangle():
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """init"""
        self.width = width
        self.height = height

    @property
    def width(self):
        "width getter"
        return self.__width

    @width.setter
    def width(self, value):
        "width setter"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        "height getter"
        return self.__height

    @height.setter
    def height(self, value):
        "height setter"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        "returns rectangle area"
        return self.__height * self.__width

    def perimeter(self):
        "returns perimeter"
        if self.height == 0 or self.area == 0:
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        "representation of rectangle"
        a = ""
        if self.__width == 0 or self.__height == 0:
            return a
        for i in range(self.__height):
            a += "#" * self.__width + "\n"
        return a
