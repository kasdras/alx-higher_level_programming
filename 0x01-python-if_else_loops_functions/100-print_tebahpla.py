#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        print("{}".format(chr(i-32)), sep="", end="")
    else:
        print("{}".format(chr(i)), sep="", end="")
