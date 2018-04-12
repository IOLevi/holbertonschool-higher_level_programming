#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv)
    if a == 1:
        print("0 arguments.")
    elif a == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        for i in range(1, a):
            print("{} arguments:".format(a - 1))
            print("{}: {}".format(i, sys.argv[i]))
