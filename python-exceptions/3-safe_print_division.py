#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        resultado = a / b
    
    except (TypeError, ValueError):
        pass
    return resultado
