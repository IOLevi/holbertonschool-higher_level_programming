#!/usr/bin/python3
'problem 15'


def pascal_triangle(n):
    'creates a pascal triangle'

    pt = [[1 for i in range(row + 1)] for row in range(n)]

    for i in range(n):
        for a in range(i):
            if a == 0 or i == a:
                pt[i][a] = 1
            else:
                pt[i][a] = pt[i-1][a-1] + pt[i-1][a]

    for i in pt:
        print(i)
