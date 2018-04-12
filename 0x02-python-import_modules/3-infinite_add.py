#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = sum((int(j) for i in range(1, len(sys.argv)) for j in sys.argv[i]))
    print(a)
