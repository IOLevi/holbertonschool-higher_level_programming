#!/usr/bin/python3
'problem 0'


def read_file(file="a", encoding="utf-8"):
    'reads a file'
    with open(file) as a:
        for line in a:
            print(line, end="")
