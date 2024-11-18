#!/usr/bin/python3
"""
say my name
"""


def say_my_name(first_name, last_name=""):
    """Prints a square of '#' characters of the given size.

    Args:
        first_name: the name of the person.
        last_name: the last name of the person.
    Raises:
        TypeError: If `firt_name` is not string
        TypeError: If `last_name` is not sting.
    """
    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
