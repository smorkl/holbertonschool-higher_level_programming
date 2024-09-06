#!/usr/bin/python3


def pow(a, b):
    if a < 0:
        a = a * -1

    if b < 0:
        b = b* -1
        c = 1 / a ** b
    else:
        c = a ** a

    return c
