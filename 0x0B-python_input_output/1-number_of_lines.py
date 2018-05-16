#!/usr/bin/python3
'problem 1'


def number_of_lines(filename=""):
    'gets number of lines in a file'
    with open(filename, encoding="utf-8") as a:
        linenumber = 0
        for line in a:
            linenumber += 1
        return linenumber
