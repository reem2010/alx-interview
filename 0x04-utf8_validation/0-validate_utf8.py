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
        data[i] = data[i] & 0xFF
    i = 0    
    while i < len(data):
        if 194 <= data[i] <= 223 and i < len(data) - 1:
            if not (128 <= data[i + 1] <= 191):
                return False
            i += 2
        elif 224 <= data[i] <= 239 and i < len(data) - 2:
            if not(128 <= data[i + 1] <= 191 and 128 <= data[i + 2] <= 191):
                return False
            i += 3
        elif 240 <= data[i] <= 247 and i < len(data) - 3:
            if not(all(128 <= byte <= 191 for byte in data[i+1:i+4])):
                return False
            i += 4
        elif not(data[i] <= 127):
            return False
        else:
            i += 1
    return True
