#!/usr/bin/python3
'problem 10'
import sys

save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

with open("add_item.json", "ra", encoding="utf-8") as a:
    new = load(a)
    for i, d in enumerate(sys.argv):
        if i > 0:
            new.append(d)
    save(new, a)
