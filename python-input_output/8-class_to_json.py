#!/usr/bin/python3
"""
class_to_json
"""


def class_to_json(obj):
    """
    Converts an object's attributes into a JSON-serializable dictionary.

    This function returns the `__dict__` attribute of the given object,
    which contains all the attributes of the object that are defined
    in the object's `__init__` method and are JSON-serializable.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing all attributes of the object.
    """
    return (obj.__dict__)