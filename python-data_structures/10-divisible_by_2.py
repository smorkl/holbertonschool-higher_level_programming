#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 within a given list.

    Args:
        my_list: An input list of integers.

    Returns:
        A new list of Boolean values (True if the corresponding
        element in the input list is a multiple of 2, False otherwise).
        The new list has the same size as the original list.
    """
    list_divisible = []
    for num in my_list:
        if num % 2 == 0:
            list_divisible.append(True)
        else:
            list_divisible.append(False)
    return list_divisible
