#!/usr/bin/python3
'problem 8'


class BaseGeometry():

    'base geo class'

    def area(self):
        'prints area'
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        'validates integers'
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/1-my_list.txt")
