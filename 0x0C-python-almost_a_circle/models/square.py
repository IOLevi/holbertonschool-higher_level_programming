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
