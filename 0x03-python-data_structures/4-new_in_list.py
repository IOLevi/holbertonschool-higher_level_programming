#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list[:]
    if idx >= len(mylist):
        return my_list[:]
    return my_list[:idx] + [element] + my_list[idx + 1:]

