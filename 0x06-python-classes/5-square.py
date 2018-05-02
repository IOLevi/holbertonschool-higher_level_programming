#!/usr/bin/python3


class Square():
    """square class"""

    def __init__(self, size=0):
        """instantiation"""
        self.__size = size

    def area(self):
        """returns square area"""
        return self.__size ** 2

    def my_print(self):
        """prints a square of the area"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")

    @property
    def size(self):
        """getter for __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
