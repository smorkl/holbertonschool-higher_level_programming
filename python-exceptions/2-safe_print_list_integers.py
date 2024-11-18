#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            element = i
            if i <= x:
                if int(element):
                    print("{:d}".format(element), end="")
                    count += 1
            else:
                break
        except (ValueError, TypeError, IndexError):
            continue
    print()
    return count
