#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints each element of a 2D integer matrix in a separate line.

    Args:
        matrix: A 2D list of integers (optional, defaults to an empty list).
    """
    for row in matrix:
        print("{:d}".format(*row))
