#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Actualiza el valor de una clave en un diccionario,
    agregándola si no existe.

    Args:
        a_dictionary (dict): El diccionario a actualizar.
        key (hashable): La clave a actualizar o agregar.
        value (any): El nuevo valor para la clave.
    """
    if key in a_dictionary:
        a_dictionary[key] = value
        return a_dictionary
    else:
        a_dictionary[key] = value
        return a_dictionary
