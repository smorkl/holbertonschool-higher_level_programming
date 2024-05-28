#!/usr/bin/python3

def multiplicar_por_2(a_diccionario):
    """
    Creates a new dictionary with values doubled from the original dictionary.

    Args:
        a_diccionario (dict): The input dictionary.

    Returns:
        dict: A new dictionary with values multiplied by 2.
    """
    new_diccionario = a_diccionario.copy()
    for key, value in new_diccionario.items():
        new_diccionario[key] = value * 2
    return new_diccionario
