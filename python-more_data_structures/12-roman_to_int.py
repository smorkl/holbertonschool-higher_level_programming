#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral string to an integer.

    Args:
        roman_string: The Roman numeral string to convert.

    Returns:
        The integer value of the Roman numeral string.
        Returns 0 for invalid input.
    """

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = roman_dict.get(char, 0)

        if value > prev_value:
            result -= value
        else:
            result += value

        prev_value = value

    return result * -1