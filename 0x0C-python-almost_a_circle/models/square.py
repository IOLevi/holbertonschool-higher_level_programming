#!/usr/bin/python3
'square module'
from .rectangle import Rectangle


class Square(Rectangle):
    'square class'

    def __init__(self, size, x=0, y=0, id=None):
        "init"
        super().__init__(size, size, x, y, id)

    def __str__(self):
        "to string for square"
        return "[SQUARE] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        'size getter'
        return self.height

    @size.setter
    def size(self, value):
        "size setter"
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        "assigns an argument to each attribute"
        p = len(args)
        if p > 0:
            self.id = args[0]

        if p > 1:
            self.size = args[1]

        if p > 2:
            self.x = args[2]

        if p > 3:
            self.y = args[3]

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
        b['size'] = b['height']
        b.pop('height')
        b.pop('width')
        return b
