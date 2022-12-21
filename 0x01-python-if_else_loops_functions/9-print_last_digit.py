#!/usr/bin/python3
def print_last_digit(number):
    rem = number % 10
    if number < 0:
        number = number * -1
        rem = number % 10
        print("{}".format(rem), sep="", end="")
    else:
        print("{}".format(rem), sep="", end="")
    return rem
