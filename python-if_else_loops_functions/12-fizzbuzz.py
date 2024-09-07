#!/usr/bin/python3

def fizzbuzz():
    """Imprime los numeros del 1 al 100, siguiendo las reglas de FizzBuzz, separados por espacios.

    """
    resultado = ""  # Inicializamos la variable resultado
    for numero in range(1, 101):
        if numero % 15 == 0:
            resultado += "FizzBuzz "
        elif numero % 3 == 0:
            resultado += "Fizz "
        elif numero % 5 == 0:
            resultado += "Buzz "
        else:
            resultado += str(numero) + " "

    # Eliminamos el último espacio extra
    resultado = resultado.rstrip()
    print(resultado)