#!/usr/bin/python3
"""
Lookup
"""


def lookup(obj):
    """Returns a dictionary containing the attributes and methods of an object.

    Args:
        obj: The object to be inspected.

    Returns:
        A dictionary where keys are attribute or method names and values are
        their types (str for attributes, function for methods).
    """
    return dir(obj)
