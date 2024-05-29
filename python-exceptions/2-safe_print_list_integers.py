#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            element = i
            if int(element):
                print("{:d}".format(element), end=" ")
                count += 1
            else:
                continue
        return count
    except (ValueError, TypeError):
        return count
