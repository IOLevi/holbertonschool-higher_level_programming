#!/usr/bin/python3
import json
from .rectangle import Rectangle
from .square import Square


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
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        "save a list of dictionaries to a file in json"
        with open("{}.json".format(cls.__name__), "w") as a:
            ldict = []
            for i in list_objs:
                ldict.append(i.to_dictionary())
            p = cls.to_json_string(ldict)
            a.write(p)
    
    @staticmethod
    def from_json_string(json_string):
        "returns a list of the JSON string"
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        o = cls.__name__
        if o == "Rectangle":
            a = Rectangle(0, 0)
        else:
            a = Square(1) #only setting size, should be 0 before update?
        a.update(**dictionary)
        return a
                
