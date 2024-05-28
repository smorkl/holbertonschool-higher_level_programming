#!/usr/bin/python3#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    ordered_keys = []

    for key in a_dictionary.keys():
        ordered_keys.append(key)
        print("{:s} {:s}".format(ordered_keys, key))