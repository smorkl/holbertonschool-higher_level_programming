#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_division = []
    shorter_list = min(len(my_list_1), len(my_list_2))
    try:
        for i, ii in zip(my_list_1[:shorter_list], my_list_2[:shorter_list]):
            result = i / ii
            my_division.append(result)
    except ZeroDivisionError:
        return None
    return my_division
