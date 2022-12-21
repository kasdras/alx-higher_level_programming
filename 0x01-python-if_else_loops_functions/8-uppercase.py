#!/usr/bin/python3
def uppercase(str):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    output = ""
    # loops through the parameter str
    for char in str:
        # loops through the alphabets
        if char in alp:
            # returns the unicode value of the character
            uniChar = ord(char)
            charValue = uniChar - 32
            output = output+chr(charValue)
        else:
            output = output+char
    print("{}".format(output))
