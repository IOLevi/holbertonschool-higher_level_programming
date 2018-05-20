#!/usr/bin/python3
"rectangle module"
from .base import Base


class Rectangle(Base):
    "rectangle class"

    def __init__(self, width, height, x=0, y=0, id=None):
        "init"
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        "height getter"
        return self.__height

    @height.setter
    def height(self, value):
        "height setter"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def width(self):
        "width getter"
        return self.__width

    @width.setter
    def width(self, value):
        "width setter"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def x(self):
        "width getter"
        return self.__x

    @x.setter
    def x(self, value):
        "width setter"
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        "y getter"
        return self.__y

    @y.setter
    def y(self, value):
        "y setter"
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        'returns the area value'
        return self.height * self.width

    def display(self):
        "prints a graphical rectangle"
        for i in range(self.y):
            print()
        for row in range(self.height):
            for i in range(self.x):
                print(" ", end="")
            print("#" * self.width)

    def __str__(self):
        'returns string of rectangle'
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        "assigns an argument to each attribute"
        p = len(args)
        if p > 0:
            self.id = args[0]

        if p > 1:
            self.width = args[1]

        if p > 2:
            self.height = args[2]

        if p > 3:
            self.x = args[3]

        if p > 4:
            self.y = args[4]

        if p > 0:
            pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        b = dict(self.__dict__)
        for key in self.__dict__:
            if key.startswith("_Rectangle"):
                b[key[12:]] = b.pop(key)
        return b
