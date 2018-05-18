#!/usr/bin/python3

from .base import Base
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def height(self):
        return self._height_
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        else:
            self.__width = value

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise ValueError("x must be an integer")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y
    @y.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("y must be an integer")
        else:
            self.__y = value

