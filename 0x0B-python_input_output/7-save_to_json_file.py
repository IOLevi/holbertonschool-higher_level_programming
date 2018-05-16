#!/usr/bin/python3
'problem 8'
import json


def save_to_json_file(my_obj, filename):
    'writes an Object to a text file, using a JSON rep'
    j = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as a:
        a.write(j)
