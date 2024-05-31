#!/usr/bin/python3

def raise_exception():
    try:
        list = ['d', 'd', 'f']
        for i in list:
            print("{}".format(list(i)))
    except TypeError:
        print("Exception has been raised")
