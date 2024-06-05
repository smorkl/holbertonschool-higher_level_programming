#!/usr/bin/python3
"""
Defines an empty Rectangle class.

"""


class Rectangle:
    """
    An immutable Rectangle class representing
    a rectangle with a width and height.

    Attributes:
        width (int, non-negative): The width of the rectangle. Must be a
            non-negative integer.
        height (int, non-negative): The height  of the rectangle. Must be a
            non-negative integer.

    Raises:
        ValueError: If the width is less than zero.
        TypeError: If the width is not an integer.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object.

        This method is called automatically when you create a new
        `Rectangle` object.
        It sets the initial width and height of the rectangle.

        Args:
            width (int, optional): The initial width of the rectangle.
              Defaults to 0.
            height (int, optional): The initial height of the rectangle.
              Defaults to 0.

        Raises:
            ValueError: If either width or height is less than zero.
            TypeError: If either width or height is not an integer.
        """
        try:
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height
        except TypeError:
            raise TypeError("height must be an integer")
        try:
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
        except TypeError:
            raise TypeError("width must be an integer")

    @property
    def width(self):
        """
        return the valor of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        In this function we handle two kinds
        of errors if width is less than 0 and if width is not an integer
        """
        try:
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        except TypeError:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        return the valor of return height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        In this function we handle two kinds
        of errors if height is less than 0 and if height is not an integer
        """
        try:
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        except TypeError:
            raise TypeError("height must be an integer")

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float: The calculated area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            float: The calculated perimeter of the rectangle.
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        using the character '#'.
        """
        output = ""
        if self.height == 0 or self.width == 0:
            return output
        else:
            char = '#'
            count = 0
            for h in range(self.height):
                for w in range(self.width):
                    output += char
                    output += ""
                count += 1
                if count == self.height:
                    return output
                else:
                    output += "\n"

    def __repr__(self):
        """
        Return the width and the height of the rectangle
        """
        return (f"Rectangle({self.width}, {self.height})")
