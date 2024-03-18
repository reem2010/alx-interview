#!/usr/bin/python3
"""lock boxes module"""


def canUnlockAll(boxes):
    """Lockboxes
    Args:
        boxes: boxes to check if it can be unlocked
    Returns:
        true or false
    """
    key = {0}
    for i in range(len(boxes)):
        if i not in key:
            return False
        for j in range(len(boxes[i])):
            key.add(boxes[i][j])        
    return True
