#!/usr/bin/python3
'problem 10'
import sys

save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

try:
    new = load('add_item.json')
except BaseException:
    new = []
for i, d in enumerate(sys.argv):
    if i > 0:
        new.append(d)
    save(new, 'add_item.json')
