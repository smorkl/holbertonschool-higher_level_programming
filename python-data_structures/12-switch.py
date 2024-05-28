#!/usr/bin/python3
a, b = 89, 10
temp = a
a = b, b = temp
print("a={:d} - b={:d}".format(a, b))