#!/usr/bin/python3
"""
d
"""

def say_my_name(first_name, last_name=""):
    """
    dd
    """
    if not isinstance(first_name, (str)) and not isinstance(last_name, (str)):
        raise TypeError("first_name must be a string or last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
