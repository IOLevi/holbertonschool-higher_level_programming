#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase"""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            num = 32
        else:
            num = 0
        print("{}".format(chr(ord(i) - num)), end='')
    print()
uppercase("this is a test 95")