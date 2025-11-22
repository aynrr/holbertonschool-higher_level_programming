#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
#Creating a new function that prints matrix of integers.
    for list in matrix:
#At first, we create a loop that iterates over the matrix of list.
        for element in list:
#Then ,we create a new loop that iterates over the elements which is located inside the matrix.
            i = list.index(element)
            if ((i == len(list))):
                print("{:d}".format(element), end="")
            else:
                print("{:d}".format(element), end=" ")
        print(end="\n")
