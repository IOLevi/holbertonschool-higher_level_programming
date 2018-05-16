#!/usr/bin/python3
'problem 5'


def append_write(filename="", text=""):
    'writes text in append mode'
    with open(filename, "a", encoding="utf-8") as a:
        p = a.write(text)
        return p
