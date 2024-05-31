#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_division = []
    try:
        for i, ii in zip(my_list_1[:list_length], my_list_2[:list_length]):
            result = i / ii
            my_division.append(result)
    except ZeroDivisionError:
        my_division.append(0)
        print("division by 0")
        continue
    except TypeError:
        my_division.append(0)
        print("wrong type")
        continue
    except IndexError:
        my_division.append(0)
        print("out of range")
        continue
    finally:
        pass
    return my_division
