#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    existe_key = key in a_dictionary
    new_key = {key: value}
    if existe_key is True:
        a_dictionary.update(new_key)
    else:
        a_dictionary.update(new_key)
 