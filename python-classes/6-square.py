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

        if (isinstance(position, tuple) and len(position)) == 2 and isinstance(position[1], int) and isinstance(position[0], int) and position[0] >= 0 and position[1] >= 0:
            self._position = position 
        else:
            raise TypeError("position must be a tuple of 2 positive integers")  
    
    @property
    def size(self):
        """
        Gets the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self._size
    
    
    @property
    def position(self):
        """
        Gets the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self._position

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

    @position.setter
    def position(self, new_position):
        """
        Sets the position of the square.

        Args:
            new_position (tupla): The new tupla to set.

        Raises:
            TypeError: If the provided is to tupla
            TypeError: if the tupla provided is to must of 2 number
            ValueError: if the elements that the tuple has are positive
        """
        if not isinstance(self._position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(self.position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(element, int) for element in new_position):
            raise ValueError("position must be a tuple of 2 positive integers")
        self._position = new_position
    
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
