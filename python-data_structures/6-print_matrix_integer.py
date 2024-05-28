#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints each element of a 2D integer matrix in a separate line.

    Args:
        matrix: A 2D list of integers (optional, defaults to an empty list).
    """
    for row in matrix:
        print(*row)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)