#!/usr/bin/python3
"""
Represents a square.

Attributes:
    __size (int): The side length of the square.

Args:
    size (int): The initial side length of the square.
"""


class Square:
    """square"""

    def __init__(self, size):
        """
        Initializes a new Square object.

        Args:
            size (int): The side length of the square.
        """
        self.__size = size