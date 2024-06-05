#!/usr/bin/python3
"""
Defines an empty Rectangle class.

"""


class Rectangle:
    """
    An immutable Rectangle class representing a rectangle with a width and height.

    Attributes:
        width (int, non-negative): The width of the rectangle. Must be a
            non-negative integer.
        height (int, non-negative): The height  of the rectangle. Must be a
            non-negative integer.

    Raises:
        ValueError: If the width is less than zero.
        TypeError: If the width is not an integer.
    """

    def __init__ (self, width=0, height=0):
        """
        Initializes a Rectangle object.

        Args:
            width (int, optional): The initial width of the rectangle. Defaults to 0.
            height (int, optional): The initial height of the rectangle. Defaults to 0.
        """
        self._width = width
        self._height = height
    
    def get_width(self):
        """
        return the valor of width
        """
        return self._width
    
    def set_width(self, value):
        """
        In this function we handle two kinds
        of errors if width is less than 0 and if width is not an integer
        """
        try:
            if value < 0:
                raise ValueError("width must be >= 0")
            self._width = value
        except TypeError:
            raise TypeError("width must be an integer")
    
    def get_height(self):
        """
        return the valor of return height
        """
        return self._height
    
    def set_height(self, value):
        """
        In this function we handle two kinds
        of errors if height is less than 0 and if height is not an integer
        """
        try:
            if value < 0:
                raise ValueError("height must be >= 0")
            self._height = value
        except TypeError:
            raise TypeError("height must be an integer")
