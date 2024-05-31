#!/usr/bin/python3
"""Square Class

square class

"""


class Square:
    """
    This class represents a square shape.

    Currently, it defines a constructor (`__init__`) that
    takes a single argument called `size` and attempts to
    create a Square object with that size. The constructor
    includes error handling to ensure the provided `size` is a valid
    integer and non-negative.

    **Valid Size:**

    The `size` argument should be an integer greater than
    or equal to zero.
    This represents the length of a side of the square.

    **Error Handling:**

    - If the provided `size` is not an integer, a `TypeError`
      is raised, and an error message is printed indicating that
      the size must be an integer.
    - If the provided `size` is less than zero (negative), a `ValueError`
      is raised, and an error message is printed indicating that the size
      must be non-negative.

    If the `size` is valid, it's assigned to a private attribute named
    `__size`. Private attributes in Python follow the convention of
      being prefixed with double underscores (`__`). While not truly
    private (they can still be accessed indirectly), this convention
    discourages direct access and promotes
    encapsulation.
    """

    def __init__(self, size):
        """
        The constructor of the Square class.

        This method is called automatically whenever
        you create a new Square object.
        It takes one argument:

        - size (int): The size of the square.
          This represents the length of a side
          of the square.

        The constructor performs the following steps:

        1. **Type Checking:** It checks if the provided `size`
          is an integer using
           `isinstance()`. If it's not an integer,
            a `TypeError` is raised.

        2. **Value Checking:** If the `size` is an integer,
          it further checks if
           it's less than zero (negative) using an `if`
           statement. If it's negative,
           a `ValueError` is raised.

        3. **Valid Size:** If both checks pass (integer and non-negative), the
           `size` is assigned to the private attribute `__size`.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
