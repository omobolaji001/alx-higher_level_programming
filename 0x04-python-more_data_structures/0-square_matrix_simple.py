#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([j**2 for j in matrix[i]])

    return new_matrix
