#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if key in sorted(a_dictionary):
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
 