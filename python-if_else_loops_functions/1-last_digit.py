#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
number2 = number
if number < 0:
    number2 = number * -1

last_digit = number2 % 10

if last_digit > 5:
    # If the number is greater than 5
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    # If the number is less than 6
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
else:
    # if the number is 0
    print(f"Last digit of {number} is {last_digit} and is 0")
