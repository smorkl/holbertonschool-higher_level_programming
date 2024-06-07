#!/usr/bin/python3
"""
function determines whether an object was inherited or not
"""


def inherits_from(obj, a_class):
    """
    if the object is an instance of the class returns true otherwise false
    """
    if (isinstance(obj, a_class)) and issubclass(type(obj), a_class):
        return True
    else:
        return False
