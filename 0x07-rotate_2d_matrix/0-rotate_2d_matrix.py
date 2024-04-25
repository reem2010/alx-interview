#!/usr/bin/python3
"""rotate 2d"""


def rotate_2d_matrix(matrix):
    """rotate 2d"""
    matrix[:] = matrix[::-1]
    mat = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    matrix[:] = mat
