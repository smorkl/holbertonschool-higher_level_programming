#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_division = []
    try:
        for i in range(min(len(my_list_1), len(my_list_2), list_length) if list_length else len(my_list_1)):
            result = my_list_1[i] / my_list_2[i]
            my_division.append(result)
    except ZeroDivisionError:
        my_division.append(0)
        print("division by 0")
    except TypeError:
        my_division.append(0)
        print("wrong type")
    except IndexError:
        my_division.append(0)
        print("out of range")
    finally:
        pass

    return my_division