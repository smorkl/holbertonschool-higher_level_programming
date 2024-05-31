#!/usr/bin/python3


class Square:
    """
    This class represents a square shape.

    Currently, it defines a constructor (`__init__`)that takes
    a single argument called `size` and assigns it to a private
    attribute named `__size`. Private attributes in Python follow
    the convention of being prefixed with double underscores (`__`).

    While not truly private (they can still be accessed indirectly), this
    convention discourages direct access and promotes encapsulation, where
    internal data is protected and accessed through methods.
    """

    def __init__(self, size):
        """
        The constructor of the Square class.

        This method is called automatically whenever
        you create a new Square object. It takes one argument:

        - size (int): The size of the square. This could
        represent the length of a side of the square.

        The constructor assigns the provided `size` to a
        private attribute named `__size`. It doesn't perform
        any additional calculations or checks in this basic
        implementation.
        """

        self.__size = size
