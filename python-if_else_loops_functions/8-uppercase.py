#!/usr/bin/python3
def uppercase(str):
    strnew = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            i = ord(i) - 32
            strnew += chr(i)
        else:
            new += i
    print("{}".format(strnew))
