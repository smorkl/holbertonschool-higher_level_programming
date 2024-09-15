#!/usr/bin/python3


def best_score(a_dictionary):
    # Iterando sobre los valores
    best_value = 0
    best_key = None
    for key, value in a_dictionary.items():
        if value > best_value:
            best_key = key
            best_value = value


a_dictionary = {"John": 12, "Bob": 14, "Mike": 14, "Molly": 16, "Adam": 10}
