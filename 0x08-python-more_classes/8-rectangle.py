#!/usr/bin/python3
"""rectangle module"""


class Rectangle():
    """rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """init"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        "string representation of rectangle"
        a = ""
        if self.__width == 0 or self.__height == 0:
            return a
        for i in range(self.__height):
            a += "#" * self.__width
            if i < self.__height - 1:
                a += '\n'
        return a

    def __repr__(self):
        "code representation of a rectangle"
        return "Rectangle(" + str(self.__width) + \
            ", " + str(self.__height) + ")"

    def __del__(self):
        "deleter"
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        "compared rectangles"
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
