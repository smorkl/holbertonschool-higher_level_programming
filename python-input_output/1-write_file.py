#!/usr/bin/python3
"""write file
"""


def write_file(filename="", text=""):
    """
    Writes the provided text to the specified file.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        write = file.weite(text)
    return write
