#!/usr/bin/python3
"""File containing the method"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""

    # Number of bytes expected to follow the current byte
    following_bytes = 0

    for num in data:
        # Check if the current byte is a leading byte
        if following_bytes == 0:
            if num >> 7 == 0b0:
                following_bytes = 0  # 1-byte character
            elif num >> 5 == 0b110:
                following_bytes = 1  # 2-byte character
            elif num >> 4 == 0b1110:
                following_bytes = 2  # 3-byte character
            elif num >> 3 == 0b11110:
                following_bytes = 3  # 4-byte character
            else:
                return False  # Invalid leading byte
        else:
            # Check if the current byte is a following byte
            if num >> 6 == 0b10:
                following_bytes -= 1
            else:
                return False  # Invalid following byte

    # Check if there are missing bytes at the end
    return following_bytes == 0
