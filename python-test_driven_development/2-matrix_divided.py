#!/usr/bin/python3
"""
Divides a matrix by a number. Handles type checking and row length consistency.
"""


def matrix_divided(matrix, div):
    """Divides all elements in a matrix by a number.

    Args:
        matrix (list of lists): A 2D list representing the matrix.
        div (int/float): The number to divide by.

    Returns:
        list of lists: A new matrix with elements divided by div.
        None: If any element in the matrix is not an int or float, or if rows have
              different lengths.

    Raises:
        TypeError: If div is zero or of an invalid type.
    """

    if not isinstance(div, (int, float)) or div == 0:
        raise TypeError("div must be a non-zero integer or float")

    new_matrix = []
    first_row_length = len(matrix[0])  # Store length of the first row

    for row in matrix:
        if len(row) != first_row_length:
            raise TypeError("Each row of the matrix must have the same size.")

        new_row = []
        for col in range(len(row)):
            element = row[col]
            if not (isinstance(element, int) or isinstance(element, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round((element / div), 2))  # Perform division and append to new row

        new_matrix.append(new_row)

    return new_matrix