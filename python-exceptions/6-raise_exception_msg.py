#!/usr/bin/python3

def raise_exception_msg(message=""):
    try:
        print(str(message))
    except NameError:
        print("error")