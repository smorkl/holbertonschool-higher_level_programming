#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    Prints each row of a 2D integer matrix
    on a separate line, with 3 elements per row.

    Args:
        matrix: A 2D list of integers (optional,
        defaults to an empty list).
    """
    if not matrix:
        return
    else:
        for row in matrix:
            counter = 0
            for i, element in enumerate(row):
                if i < len(row) - 1:
                    print("{:d}".format(element), end=" ")
                else:
                    print("{:d}".format(element), end="\n")
                if counter == 3:
                    counter = 0
                    print()
