class Square:
    """Square class representation with methods for area calculation and size manipulation."""

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


my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
