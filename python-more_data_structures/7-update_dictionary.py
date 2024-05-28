#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    new_key = {key: value}
    existe_key = new_key in a_dictionary
    if existe_key is True:
        a_dictionary.update(new_key)
    else:
        a_dictionary.update(new_key)
 