#!/usr/bin/python3
"""
class_to_json
"""


def class_to_json(obj):
    """
    Converts an object into a JSON-serializable dictionary.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing JSON-serializable
        attributes of the object.
    """
    attributes = vars(obj)
    json_dict = {}

    for key, value in private_attributes.items():
        if isinstance(value, list):
            json_dict[key] = [item for item in value if _is_json_serializable(item)]
        elif isinstance(value, dict):
            json_dict[key] = {k: v for k, v in value.items() if _is_json_serializable(v)}
        elif isinstance(value, (str, int, bool)):
            json_dict[key] = value
        else:
            json_dict[key] = repr(value)    
    return json_dict


def _is_json_serializable(value):
    """
    Helper function to check if a value is JSON-serializable.

    Args:
        value: The value to check.

    Returns:
        bool: True if the value is JSON-serializable, False otherwise.

    """
    return isinstance(value, (str, int, bool, list, dict))
