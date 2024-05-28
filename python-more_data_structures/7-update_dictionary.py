#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    existe_key = key in a_dictionary
    if existe_key is True:
        key = a_dictionary[value]
    else:
        a_dictionary[key] = value
 