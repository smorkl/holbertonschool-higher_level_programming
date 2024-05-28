#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints the elements of a list of integers in reverse order.

    Args:
        my_list (list, optional): The list of integers to print.
        Defaults to an empty list.
    """
    for i in reversed(my_list):
        print("{:d}".format(i))
