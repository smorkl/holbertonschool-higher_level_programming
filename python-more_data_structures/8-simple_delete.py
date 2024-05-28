#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes a key from a dictionary.

    Args:
        a_dictionary (dict): The dictionary to delete the key from.
        key (str, optional): The key to delete. If no key is provided, the
        function makes no changes. Defaults to "".

    Returns:
        dict: The modified dictionary with the key deleted (if it existed). If
        the key did not exist, returns the original dictionary unchanged.
    """
    if key in a_dictionary:
        del a_dictionary[key]
        return a_dictionary
    else:
        return a_dictionary
