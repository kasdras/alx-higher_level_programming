#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    #new_list =  my_list[::-1] //another way of reversing a list
    i = 0
    while i < len(my_list) / 2:
        temp = my_list[i]
        my_list[i] = my_list[len(my_list) - i - 1]
        my_list[len(my_list) - i - 1] = temp
        i += 1
    for i in my_list:
        print("{:d}".format(i))
