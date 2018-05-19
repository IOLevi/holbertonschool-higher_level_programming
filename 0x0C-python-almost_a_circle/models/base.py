#!/usr/bin/python3
import json
class Base:
    'class Base'
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        "returns the json representation of a list of dictionaries"
        return json.dumps(list_dictionaries)
        