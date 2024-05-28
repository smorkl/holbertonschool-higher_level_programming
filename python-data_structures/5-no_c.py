#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all occurrences of the letter 'c' (case-insensitive) from a string.

    Args:
        my_string: The input string.

    Returns:
        The modified string with all 'c' characters removed.
    """
    new_string = ""
    for char in my_string:
        if char != c or char != C:
            new_string += char
    return new_string
