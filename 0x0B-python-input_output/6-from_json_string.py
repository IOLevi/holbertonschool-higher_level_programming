#!/usr/bin/python3
'problem 7'

import json
def from_json_string(my_str):
    'returns a python object represented by a JSON string'
    return json.loads(my_str)
