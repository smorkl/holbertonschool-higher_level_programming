#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    if a > 0 and b > 0:
        print("{} + {} = {}".format(a, b, add(a, b)))
