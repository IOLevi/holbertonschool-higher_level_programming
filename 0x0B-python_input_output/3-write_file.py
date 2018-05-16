#!/usr/bin/python3
'problem 4'


def write_file(filename="", text=""):
    'writes text to a file'
    with open(filename, "w", encoding="utf-8") as a:
        written = a.write(text)
        return written
