#!/usr/bin/python3
'problem 3'


def read_lines(filename="", nb_lines=0):
    'reads nb_lines number of lines from a file and prints them'
    with open(filename, encoding="utf-8") as a:
        if nb_lines == 0:
            for i in a:
                print(i, end="")
            return
        count = 0
        for i in a:
            print(i, end="")
            count = count + 1
            if count == nb_lines:
                return
