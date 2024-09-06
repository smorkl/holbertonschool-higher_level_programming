#!/usr/bin/python3
import random

num = random.randint(-10000, 10000)

if num < 0:
    numpositive = num * -1
    last_digit = numpositive % 10
else:
    last_digit = num % 10
if num < 0:
    last_digit = last_digit * -1
if last_digit > 5:
    # If the num is greater than 5
    print(f"Last digit of {num} is {last_digit} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    # If the num is less than 6
    print(f"Last digit of {num} is {last_digit} and is less than 6 and not 0")
else:
    # if the num is 0
    print(f"Last digit of {num} is {last_digit} and is 0")
