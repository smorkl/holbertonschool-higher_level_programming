#!/usr/bin/python3
"""
to json string
"""
import json


def to_json_string(my_obj):
    """Converts a Python object to its JSON representation (string).

    Args:
        my_obj: The Python object to convert.

    Returns:
        The JSON string representation of the object, or None if the object
        cannot be serialized to JSON.
    """

    return json.dumps(my_obj)
