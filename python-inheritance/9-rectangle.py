#!/usr/bin/python3
"""
Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle with width and height attributes.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle object.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height are not strictly positive.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height

    def __str__(self):
        return f"[Rectangle] {self._width}/{self._height}"

    def area(self):
        result = (self._width * self._height)
        return result
