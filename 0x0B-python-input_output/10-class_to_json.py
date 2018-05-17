#!/usr/bin/python3
'problem 11'


def class_to_json(obj):
    """returns the dict description with simple data structure
    for JSON serialization of an object"""
    return obj.__dict__
