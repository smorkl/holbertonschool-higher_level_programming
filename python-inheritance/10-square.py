#!/usr/bin/python3
"""
square that inherits from rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Represents a square with size attributes.
    """

    def __init__(self, size):
        """
        Initializes a square object.

        Args:
        size (int): The size of the square.

        Raises:
        TypeError: If size is  not an integer.
        ValueError: If size is not strictly positive.
        """
        super().integer_validator("size", size)
        self._size = size

    def area(self):
        result = self._size**2
        return result
