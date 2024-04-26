#!/usr/bin/python3
"""minoperations"""


def minOperations(n):
    """
    In a text file, there is a single character H.
    Your text editor can execute only two
    operations in this file
    """
    if n <= 1:
        return 0
    op = 0
    div = 2
    while n > 1:
        while n % div == 0:
            op += div
            n //= div
        div += 1

    return op
