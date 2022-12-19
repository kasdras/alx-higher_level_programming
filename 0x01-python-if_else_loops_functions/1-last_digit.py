#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
str = "Last digit of {} is {} and is"
str1 = "greater than 5"
str3 = "0"
str4 = "less than 6 and not 0"
if number < 0:
    positiveNum = number * -1
    change = positiveNum % 10
    if change == 0:
        print(str.format(number, change), str3)
    else:
        str = "Last digit of {} is -{} and is"
        print(str.format(number, change), str4)
else:
    if lastDigit > 5:
        print(str.format(number, lastDigit), str1)
    elif lastDigit < 6 and lastDigit != 0:
        print(str.format(number, lastDigit), str4)
    else:
        print(str.format(number, lastDigit), str3)
