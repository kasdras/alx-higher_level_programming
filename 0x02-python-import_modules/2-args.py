#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(argv)
    i = 1
    if n == 1:
        print("{} argument.".format(0))
    elif n == 2:
        print("{} argument:".format(i))
        print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(n-i))
        while i < n:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
