#!/usr/bin/python3
'problem 9'
import json


def load_from_json_file(filename):
    'creates an Object from a JSON file'
    with open(filename, encoding="utf-8") as a:
        json.load(a)
