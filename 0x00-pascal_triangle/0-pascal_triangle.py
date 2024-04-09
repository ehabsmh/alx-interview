#!/usr/bin/python3
"""Representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n
       @n: number of rows
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(n - 1):
        row = [1]  # prepend 1

        for j in range(i):
            row.append(triangle[i][j] + triangle[i][j + 1])  # calculate

        row.append(1)  # append 1
        triangle.append(row)

    return triangle
