#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        resultado = a / b
        return resultado
    except (TypeError, ValueError):
        return None
    finally:
        return None
