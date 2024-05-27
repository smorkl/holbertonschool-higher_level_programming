#!/usr/bin/python3

import sys


def add_num(args):

    list_int = [int(x) for x in args[1:]]
    add_total = 0
    if len(list_int) > 1:
        for add in list_int:
            add_total += add
        print(f"{add_total}")
    else:
        print(len(args))


if __name__ == "__main__":
    add_num(sys.argv)
