#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_division = []
    try:
        for i in range(list_length):
            result = my_list_1[i] / my_list_2[i]
            my_division.append(result)
    except ZeroDivisionError:
        my_division.append(0)  # Replace None with 0 for better behavior
        print("division by 0")
    except TypeError:
        my_division.append(0)  # Replace None with 0 for better behavior
        print("wrong type")
    except IndexError:
        my_division.append(0)  # Replace None with 0 for better behavior
        print("out of range")
    finally:
        pass  # Add cleanup actions if needed
    return my_division
