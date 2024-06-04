#!/usr/bin/python3
"""
    add two number
"""

def add_integer(a, b=98):
    """Adds two integers together.

    Args:
        a: The first integer to add. (required)
        b: The second integer to add. Defaults to 98. (optional)

    Returns:
        The sum of the two integers.

    Raises:
        TypeError: If either a or b is not an integer.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")

    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    else:
        a = round(int(a))
        b = round(int(b))
        return (a + b)
