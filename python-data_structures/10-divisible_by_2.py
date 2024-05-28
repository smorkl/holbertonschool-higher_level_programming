#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Finds elements in a list that are divisible by 2 (even numbers).

    Args:
        my_list: An optional list of numbers (defaults to an empty list).

    Returns:
        A new list containing elements from the input list
        that are divisible by 2.
    """
    list = []
    for num in my_list:
        if num % 2 == 0:
            list.append(num)
    return list