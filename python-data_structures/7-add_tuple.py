#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        print("{:d}".format(tuple_a(0) + tuple_b(0), end=" "))
        print("{:d}".format(0 + tuple_b(1), end="\n"))
    elif len(tuple_b) < 2:
        print("{:d}".format(tuple_a(0) + tuple_b(0), end=" "))
        print("{:d}".format(tuple_a(1) + 0, end="\n"))
    else:
        print("{:d}".format(tuple_a(0) + tuple_b(0), end=" "))
        print("{:d}".format(tuple_a(1) + tuple_b(1), end="\n"))        