#!/usr/bin/python3
"""
"""


def append_write(filename="", text=""):
    """Appends text to the end of a file in UTF-8 encoding.

    Args:
        filename: The name of the file to append to.
        text: The text to append to the file.

    Returns:
        The number of characters appended to the file.
    """

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
