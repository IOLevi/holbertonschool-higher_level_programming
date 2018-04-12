#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        a = sum((int(j) for i in range(1, len(sys.argv)) for j in sys.argv[i]))
        print(a)
