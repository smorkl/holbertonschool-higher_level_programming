#!/usr/bin/python3
"""Square Class

square class

"""


class square:
    """square class

    methods for manipulation

    """

    def __init__(self, size=0):
        """
        Initializes a new Square object.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than zero.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The calculated area of the square.
        """
        return self.__size ** 2
