#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    f = 0
    for i, d in enumerate(sys.argv):
        if i > 0:
            f += d
    print(d)
