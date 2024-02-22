#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotate matrix 90 degrees clockwise"""
    c = 0
    for i in range(len(matrix)):
        j = i
        while j < (len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            j = j + 1
    for row in matrix:
        row.reverse()
