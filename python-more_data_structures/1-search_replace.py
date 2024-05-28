#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = [replace if x == search else x for x in my_list]

    return(new_list)

my_list = [1, 2, 3, 4, 5]
search = 3
replace = 10

new_list = search_replace(my_list, search, replace)
print(new_list)  # Salida: [1, 2, 10, 4, 5]