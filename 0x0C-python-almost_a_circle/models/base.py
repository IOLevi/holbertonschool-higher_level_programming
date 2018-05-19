#!/usr/bin/python3
class Base:
    'class Base'
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
