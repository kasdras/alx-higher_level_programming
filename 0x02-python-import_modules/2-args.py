#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(argv)
    if n == 0:
        print("{} argument.".format(n))
    elif n == 1:
        print("{} argument:".format(n))
        print("{}: {}".format(argv[1]))
    else:
        print("{} arguments:".format(n))
        for argv_list in range(1, n):
            print("{}: {}".format(n, argv_list))
