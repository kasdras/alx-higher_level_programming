#!/usr/bin/python3
def print_matrix_integer(matrix[[]]):
    length = len(matrix)
    i = 0
    while i < length:
        j = 0
        while j < len(matrix[i]):
            if j != len(matrix[i]) - 1:
                print("{}".format(matrix[i][j]), end=' ')
            else:
                print("{}".format(matrix[i][j]))
            j += 1
        i += 1
