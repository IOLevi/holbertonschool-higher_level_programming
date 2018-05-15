#!/usr/bin/python3
'problem 5'


def is_kind_of_class(obj, a_class):
    'is subclass'
    if issubclass(obj, a_class):
        return True
    return False
