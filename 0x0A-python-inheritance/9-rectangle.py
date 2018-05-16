#!/usr/bin/python3
"problem 9"

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    "rectangle class"

    def __init__(self, width, height):
        "init"
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        "area"
        return self.__height * self.__width

    def __str__(self):
        "prints str"
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
