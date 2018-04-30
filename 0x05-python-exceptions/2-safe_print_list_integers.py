#!/usr/bin/python3
def safe_print_list_integers(my_list=[]. x=0):
    printed = 0
    try:
        for i in range(x):
            print("{:d}".format(mylist[i]), end="")
            printed += 1
    except ValueError:
        pass
    finally:
        print()
        return printed
