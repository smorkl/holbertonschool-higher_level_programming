#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tupla_c = (tuple_a[0] + tuple_b[0], tuple_b[1])
        return tupla_c
    elif len(tuple_b) < 2:
        tupla_c = (tuple_a[0] + tuple_b[0], tuple_a[1])
        return tupla_c
    elif len(tuple_a) == 0:
        return tuple_b
    else:
        tupla_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return tupla_c 
    