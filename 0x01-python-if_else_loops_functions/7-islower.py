#!/usr/bin/python3
def islower(c):
    """checks if a char is lowercase"""
    if ord(c) >= 97 and ord(c) < 123:
        return True
    else:
        return False
