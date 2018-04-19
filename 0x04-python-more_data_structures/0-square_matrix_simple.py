#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[i**2 for i in matrix[x]] for x in range(len(matrix))]
