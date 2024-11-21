#!/usr/bin/python3
"""
text identation
"""


def text_indentation(text):
    """prints a text if it finds one of these chars it makes a line break.

    Args:
        text: text(string) for print.
    Raises:
        TypeError: If `text` is not string

    """
    if not isinstance(text, (str)):
        raise TypeError("text must be a string")

    ministring = ""
    for char in text:
        ministring += char
        if char in ".?:":
            print(ministring.strip())
            ministring = ""

    if ministring:
        print(ministring.strip())
