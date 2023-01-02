#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    n = len(argv)
    i = 1
    if n == 0:
        print("{} arguments.".format(n))
    elif n == 1:
        print("{} argument:".format(n))
        print("{}: {}".format(i, sys.argv[1]))
    else:
        print("{} arguments:".format(n))
        while i <= n:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
