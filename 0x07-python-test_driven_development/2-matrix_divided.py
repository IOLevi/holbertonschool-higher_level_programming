#!/usr/bin/python3
"""matrix divided module"""


def matrix_divided(matrix, div):
    """returns new matrix with elements divided by div"""
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    thelen = len(matrix[0])

    if thelen == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != thelen:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in matrix[x]] for x in range(len(matrix))]


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/2-matrix_divided.txt")
