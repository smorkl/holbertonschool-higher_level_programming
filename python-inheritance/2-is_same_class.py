#!/usr/bin/python3
"""
way to inherit a list
"""


def is_same_class(obj, a_class):
    """
    if the object is an instance of the class returns true otherwise false
    """
    if type(obj) is a_class:
        return True
    else:
        return False
