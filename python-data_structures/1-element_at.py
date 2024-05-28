#!/usr/bin/python3

def element_at(my_list, idx):
    """Returns the element at a given index in the list.

    Args:
        my_list: The list to access.
        idx: The index of the element to retrieve.

    Returns:
        The element at the specified index, or "none"
        if the index is out of bounds.
    """
    if idx < 0 or idx >= len(my_list):
        return "none"
    else:
        return my_list[idx]
