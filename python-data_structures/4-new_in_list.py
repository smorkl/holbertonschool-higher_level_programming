#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position.

    Args:
        my_list: The list to modify.
        idx: The index of the element to replace.
        element: The new element to insert.

    Returns:
        A new list with the element replaced, or the
        original list if the index is out of range.
    """
    new_list = my_list
    if idx < 0 or idx >= len(my_list):
        return new_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
