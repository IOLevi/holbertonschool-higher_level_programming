#!/usr/bin/python3
'problem 9'


class Rectangle(__import__('7-BaseGeometry').BaseGeometry):

    'rectangle class'

    def __init__(self, width, height):
        'init'
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
