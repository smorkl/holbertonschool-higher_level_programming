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
    if not isinstance(a and b, int or float):
        raise TypeError("a must be an integer or b must be an integer")
    else:
        int(a)
        int(b)
        return (a + b)
