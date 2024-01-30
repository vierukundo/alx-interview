#!/usr/bin/python3
"""File containing the method"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    for num in data:
        if num > 127 or num < 0:
            return False
    return True
