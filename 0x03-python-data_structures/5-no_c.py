#!/usr/bin/python3
def no_c(my_string):
    while ('c' in my_string):
        i = my_string.index('c')
        my_string = my_string[:i] + my_string[i + 1:]
    while ('C' in my_string):
        i = my_string.index('C')
        my_string = my_string[:i] + my_string[i + 1:]
    return my_string
