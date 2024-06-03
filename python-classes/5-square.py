#!/usr/bin/python3
"""Square Class

square class

"""


class Square:
    """
    Square class representation with methods for
    area calculation and size manipulation.
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size  # Private attribute to store the square's size

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
        """
        Sets the size of the square.

        Args:
            new_size (int): The new size to set.

        Raises:
            ValueError: If the provided size is less than zero.
            TypeError: If the provided size is different to int
        """
        try:
            if new_size < 0:
                raise ValueError("size must be >= 0")
            self._size = new_size
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The calculated area of the square.
        """
        return self.size ** 2  # Use the property to access the size

    def my_print(self):
        """
        Prints a square matrix of '#' characters with a size based on
        the object's size attribute.
        """
        char = '#'
        for row in range(self.size):
            for colum in range(self.size):
                print(char, end="")
            print()
