#!/usr/bin/python3
'problem 12'


class Student:
    'class student'

    def __init__(self, first_name, last_name, age):
        'init'
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        'gives a dict of an obj'
        flag = False
        if isinstance(attrs, list):
            for i in attrs:
                if not isinstance(i, str):
                    flag = False
                    break
                else:
                    flag = True

        if flag:
            new = {}
            for d in attrs:  # list of strings
                new.update((d, self.__dict__[d]))
            return new
        else:
            return self.__dict__
