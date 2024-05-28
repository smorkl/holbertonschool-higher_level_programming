#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Creates a new list containing only unique elements from the input list.

    Args:
        my_list (list, optional): The input list. Defaults to an empty list.

    Returns:
        list: A new list containing the unique elements.
    """

    seen = set()
    new_list = []
    for num in my_list:
        if num not in seen:
            seen.add(num)
            new_list.append(num)

    return new_list
