#!/usr/bin/python3
'problem 15'


def pascal_triangle(n):
    'prints a pascal tringle of n height'
    if n <= 0:
        return []
    pt = [[1 for i in range(row + 1)] for row in range(n)]

    for i in range(n):
        for a in range(i + 1):
            if i == a or a == 0:
                pt[i][a] = 1
            else:
                pt[i][a] = pt[i - 1][a - 1] + pt[i - 1][a]

    for l in pt:
        print(l)
