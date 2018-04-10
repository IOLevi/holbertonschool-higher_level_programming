#!/usr/bin/python3
def print_last_digit(number):
    """prints last digit of a number"""
    if number < 0:
        number *= -1
    print("{}".format(number % 10), end='')
    return number % 10
