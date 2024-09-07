#!/usr/bin/python3

def fizzbuzz():
    """Imprime los numeros del 1 al 100, siguiendo las reglas de FizzBuzz, separados por espacios.

    """
    resultado = ""  # Inicializamos la variable resultado
    for numero in range(1, 101):
        if numero % 15 == 0:
            print("FizzBuzz", end=" ")
        elif numero % 3 == 0:
            print("Fizz", end=" ")
        elif numero % 5 == 0:
            if numero != 100:
                print("Buzz", end=" ")
            else:
                print("Buzz")        
        else:
            print(f"{numero}", end=" ")

                

fizzbuzz()