#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0  # Handle non-string or empty input

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    num = 0
    prev_value = 0

    for char in roman_string[::-1]:
        value = roman_dict.get(char, 0)

        if value < prev_value and prev_value not in (10, 100, 1000):
            return 0
        elif value <= prev_value:
            num += value
        else:
            num -= value
        prev_value = value

    return num if 1 <= num <= 3999 else 0