#!/usr/bin/python3
def print_last_digit(number):
    rem = number % 10
    if number < 0:
        print("-{}".format(rem))
    else:
        print("{}".format(rem))
