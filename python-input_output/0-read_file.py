#!/usr/bin/python3
"""read file
"""


def read_file(filename=""):
    """
    Reads the content of a file and returns it as a string.

    Args:
        filename (str, optional): The filename to open.
        Defaults to "".

    Returns:
        str: The contents of the file as a string, or an empty
        string if the file is empty or cannot be opened.
    """
    with open(filename, 'r') as file:
        contents = file.read()
        return contents
