#!/usr/bin/python3
"""
square that inherits from rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
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
        self.integer_validator("size", size)
        self._size = size

    def area(self):
        result = (self._size ** 2)
        return result

s = Square(4)
print(s.area())