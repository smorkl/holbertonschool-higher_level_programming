#!/usr/bin/python3
"""
this module defines the 'Square' class, which represents a square.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The side length of the square.

    Args:
        size (int, optional): The initial side length
        of the square. Defaults to 0.
    """

    def __init__(self, size=0) -> None:
        """
        Initializes a new Square object.

        Args:
            size (int, optional): The initial side
            length of the square. Must be a non-negative
            integer. Defaults to 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is negative.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self._size = size

    @property
    def size(self):
        """
        Gets the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self._size

    @size.setter
    def size(self, new_size):
        """pass"""
        self._size = new_size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size**2
