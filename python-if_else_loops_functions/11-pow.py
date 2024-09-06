#!/usr/bin/python3

def pow(a, b):
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    
    c = a ** a

    return c