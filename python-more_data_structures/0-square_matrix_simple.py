#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    new_matrix = []
    for row in matrix:
        new_row = [float(x * x) for x in row]
        new_matrix.append(new_row)

    return new_matrix
