#!/usr/bin/python3
def islower(i):
    """determines of char is lowercase"""
    if ord(i) >= 97 and ord(i) < 123:
        return True
    else:
        return False


def uppercase(str):
    """prints a string in uppercase"""
    for i in str:
        print("{}".format(chr(ord(i) - 32) if islower(i) else i), end='')
    print()
