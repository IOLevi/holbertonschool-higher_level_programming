#!/usr/bin/python3


class Square():
    """square class"""

    def __init__(self, size=0):
        """instantiation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns square area"""
        return self.__size ** 2