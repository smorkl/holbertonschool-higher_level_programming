#!/usr/bin/python3

def raise_exception():
    try:
        list = ['d', 'd', 'f']
        for i in list:
            print("{}".format(list(i)))
    except TypeError:
        return TypeError