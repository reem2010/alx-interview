#!/usr/bin/python3
"""UTF-8 Validation module"""


def validUTF8(data):
    """UTF-8 Validation
    Args:
        data: entred data
    Returns:
        True if data is a valid UTF-8 encoding
    """
    for i in range(len(data)):
        if data[i] >= 0 and data[i] <= 127:
            data[i] = True
        elif(data[i] & 192 and i < len(data)-1):
            data[i] = True
            data[i + 1] = True
            i = i + 1
        else:
            return False
    return True
