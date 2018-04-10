#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase"""
    for i in str:
        print("{}".format(chr(ord(i) - 32) if
                          ord(i) >= 97 and ord(i) < 123 else i), end='')
    print()
uppercase("holbertGEG 9")
