#!/usr/bin/python3

def element_at(my_list, idx):
    
    if idx < 0:
        return "none"
    elif idx > len(my_list):
        return "none"
    else:
        print(my_list(idx))
