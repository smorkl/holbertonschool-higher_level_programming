#!/usr/bin/python3


def best_score(a_dictionary):
    # Iterando sobre los valores
    best_value = 0
    best_key = None
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > best_value:
                best_key = key
                best_value = value
        return best_key
    else:
        return None
