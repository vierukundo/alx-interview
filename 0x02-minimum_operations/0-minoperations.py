#!/usr/bin/python3
"""answer file"""


def minOperations(n):
    """compute the minimum operations to achieve n H"""
    if n <= 1:
        return 0
    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n = n // divisor
            operations += divisor
            continue
        else:
            divisor += 1
    return operations
