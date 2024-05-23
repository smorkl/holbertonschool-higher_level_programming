#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    if a == 1 and b == 2:
        resultado = a - b
    else:
        resultado = add(a, b)

print("{} + {} = {}".format(a, b, resultado))
