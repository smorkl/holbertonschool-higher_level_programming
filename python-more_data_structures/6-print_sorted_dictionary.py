#!/usr/bin/python3#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for keys in sorted(a_dictionary):
        print("%s: %s" % (keys, a_dictionary[keys]))