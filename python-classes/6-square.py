#!/usr/bin/python3
"""Square Class

square class

"""


class Square:
    """
    Square class representation with methods for
    area calculation and size manipulation.
    """

    def __init__(self, size=0, position=(0, 0)):
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

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(element, int) for element in position):
            raise ValueError("all elements in position must be integers")
        self._position = position  # Use a different attribute name

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
            int: The calculated area of the square.
        """
        return self.size ** 2  # Use the property to access the size

    def my_print(self):
        """
        Prints a square matrix of '#' characters with a size based on
        the object's size attribute.

        This function attempts to print a square using '#' characters,
        considering the object's `_position` attribute
        (a tuple of two integers).

        However, there's a potential issue with the current implementation.
        """
        if self.size == 0:
            print()
        else:
            char = '#'
            for row in range(self.size):
                cout = self._position[0]
                i = 0
                while i < cout:
                    print("_", end="")
                    i += 1
                for colum in range(self.size):
                    print(char, end="")
                print("$")
