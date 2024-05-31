#!/usr/bin/python3

class Square:
    """
    This class represents a square shape.

    Currently, it only defines a constructor that prints a simple string
    representation of a square using curly braces `{}`. However, you
    can extend this class to add functionalities specific to squares,
    such as calculating area, perimeter, or drawing a more visually
    appealing representation.
    """

    def __init__(self):
        """
        The constructor of the Square class.

        When creating a Square object, this method is automatically called
        and prints the string representation of the square (`{}`).
        """
        print("{\}")  # Prints a simple representation of a square