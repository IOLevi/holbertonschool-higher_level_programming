#!/usr/bin/python3
'problem 3'


def read_lines(filename="", nb_lines=0):
    'reads nb_lines number of lines from a file and prints them'
    with open(filename, encoding="utf-8") as a:
        for i in range(nb_lines):
            print(a.readline(), end="")
