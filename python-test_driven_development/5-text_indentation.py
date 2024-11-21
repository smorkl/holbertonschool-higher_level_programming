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

    listchar = [".", "?", ":"]
    ministring = ""
    for char in text:
        ministring += char
        for i in listchar:
            if char == i:
                ministring = ministring.lstrip()
                print(ministring)
                ministring = ""
    
    if ministring:
        ministring = ministring.rtrip()
        print(ministring)
