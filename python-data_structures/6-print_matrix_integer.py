#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints each row of a 2D integer matrix on a separate line, with 3 elements per row.

    Args:
        matrix: A 2D list of integers (optional, defaults to an empty list).
    """
    for row in matrix:
        counter = 0
        for element in row:
            print("{}".format(element), end=" ")
            counter += 1
            if counter == 3:
                counter = 0
                print()
