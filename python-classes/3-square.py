#!/usr/bin/python3
"""Square Class

square class

"""


class square:
    """
    This Python script defines a `Square` class that represents
      a square shape.

    The `Square` class offers the following functionalities:

    * **Constructor (`__init__`):**
        - Initializes a new Square object with a specified size.
        - Ensures the provided size is a valid integer greater than
          or equal to zero.
        - Raises `TypeError` if the size is not an integer.
        - Raises `ValueError` if the size is negative.
        - Assigns the validated size to a private attribute named `__size`.

    * **Area Calculation (`area` method):**
        - Calculates the area of the square based on its size.
        - The area is calculated by squaring the private attribute `__size`.
        - Returns the calculated area as a floating-point number.

    **Private Attribute:**

    * `__size`: Stores the size of the square (assumed to be the side length).
    This attribute is prefixed with double underscores (`__`) to indicate it's
    considered private by convention (although technically still accessible
    indirectly).

    **Usage Example (Assuming Future Methods):**

    ```python
    my_square = Square(5)  # Create a Square with size 5
    print(my_square.area())  # Placeholder for future area calculation
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
