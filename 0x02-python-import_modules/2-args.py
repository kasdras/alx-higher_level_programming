#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = len(argv)
    i = 1
    if n == 1:
        print("0 arguments.")
    elif n == 2:
        print("1 argument:")
        print("{:d}: {:s}".format(i, argv[1]))
    else:
        print("{:d} arguments:".format(n - 1))
        while i <= n:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1
