#!/usr/bin/python3
def uppercase(str):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    # loops through the parameter str
    for char in str:
        # loops through the alphabets
        if char in alp:
            uniChar = ord(char) # returns the unicode value of the character
            charValue = uniChar - 32
            output = output+chr(charValue)
        else:
            output = output+char
    print("{}".format(output))
