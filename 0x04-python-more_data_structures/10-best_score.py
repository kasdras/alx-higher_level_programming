#!/bin/usr/python3
def best_score(a_dictionary):
    result = 0
    if a_dictionary:
        for key in a_ictionary:
            if a_dictionary[key] > result:
                result = a_dictionary[key]
                winner = key
        return winner
