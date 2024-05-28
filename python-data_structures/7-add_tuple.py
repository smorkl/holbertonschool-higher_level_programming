#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tupla_c = ()

    if len(tuple_a) < 2:
        tupla_c[0] = tuple_a[0] + tuple_b[0]
        tupla_c[1] = tuple_a[1] + tuple_b[1]
