#!/usr/bin/python3
"""
load from json file
"""
import json


def load_from_json_file(filename):
    """
    Loads an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The object decoded from the JSON file.

    Raises:
        FileNotFoundError: If the specified file is not found.
    """

    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data
