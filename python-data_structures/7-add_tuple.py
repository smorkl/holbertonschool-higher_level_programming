#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 1 and len(tuple_b) == 1:
        tupla_c = (tuple_a[0] + tuple_b[0], 0)
        return tupla_c
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            tupla_c = (tuple_a[0] + tuple_b[0], tuple_b[1])
            return tupla_c
        return tuple_b
    elif len(tuple_b) < 2:
        if len(tuple_b) == 1:
            tupla_c = (tuple_a[0] + tuple_b[0], tuple_a[1])
            return tupla_c
        return tuple_a
    elif len(tuple_a) == 0 and len(tuple_b) == 0:
        tupla_c = (0, 0)
        return tupla_c
    else:
        return tupla_c == (0, 0)