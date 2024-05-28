#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Creates a new matrix containing the elements of the input matrix squared.

    Args:
        matrix (list, optional): The input matrix. Defaults to an empty list.

    Returns:
        A new list containing the squared elements.
    """

    new_matrix = []

    new_matrix = []
    for row in matrix:
        new_row = [int(x * x) for x in row]
        new_matrix.append(new_row)

    return new_matrix
