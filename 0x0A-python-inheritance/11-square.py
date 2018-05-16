
#!/usr/bin/python3
'problem 10'

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    'square class'

    def __init__(self, size):
        'init'
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        'to string'
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
