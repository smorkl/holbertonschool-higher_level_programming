#!/usr/bin/python3

def print_square(size):
    """Prints a square of '#' characters of the given size.

    Args:
        size: The size of the square. Must be a non-negative integer.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is negative.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
        