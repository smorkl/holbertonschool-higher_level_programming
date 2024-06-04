#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, (str)) and not isinstance(last_name, (str)):
        raise TypeError("first_name must be a string or last_name must be a string")
    else:
        print("My name is {} {}$".format(first_name, last_name))

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

