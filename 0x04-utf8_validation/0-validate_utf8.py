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
        else:
            data[i] = False
    for res in data:
        if not res:
            return False
    return True
