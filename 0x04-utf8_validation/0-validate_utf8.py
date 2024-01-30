#!/usr/bin/python3
"""File containing the method"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    
    for num in data:
        # Consider only the 8 least significant bits
        num &= 0xFF
        
        # Check if the leading bit is 0 (1-byte character)
        if num >> 7 == 0b0:
            continue
        else:
            return False  # Invalid leading byte
    
    return True
