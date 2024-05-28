#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the max integer in a list.

    Args:
        my_list: An optional list of integers. Defaults to an empty list.

    Returns:
        The max int integer in the list, or "None" if the list is empty.
    """
    if not my_list:
        return "None"
    else:
        max_integer = my_list[0]
        for num in my_list:
            if num > max_integer:
                max_integer = num
        return max_integer
