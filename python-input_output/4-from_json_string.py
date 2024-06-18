#!/usr/bin/python3
"""
"""
import json


def from_json_string(my_str):
    """Parses a JSON string and returns the corresponding Python object.

    Args:
        my_str: The JSON string to parse.

    Returns:
        The Python object represented by the JSON string, or None if the
        string is empty or cannot be parsed as JSON.
    """

    return json.loads(my_str)
