#!/usr/bin/python3
'problem 5'


def inherits_from(obj, a_class):
    'is subclass'
    if issubclass(type(obj), a_class):
        return True
    return False
