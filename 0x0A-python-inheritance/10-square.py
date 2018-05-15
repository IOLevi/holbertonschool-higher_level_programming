#!/usr/bin/python3
'problem 10'


class Square(__import__('9-Rectangle').Rectangle):

    'square class'

    def __init__(self, size):
        'init'
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        'area function'
        return super().area()
