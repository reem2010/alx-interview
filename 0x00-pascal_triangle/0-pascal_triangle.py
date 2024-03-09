#!/usr/bin/python3
"""pascale triangle module"""


def pascal_triangle(n):
    """pascale triangle
    Args:
        n: number of rows
    Returns:
        pascale triangle
    """
    if n <= 0:
        return ([])
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    pascale = [[1], [1, 1]]
    for i in range(1, n):
        old = pascale[i]
        newList = [old[j] + old[j+1] for j in range(len(old)-1)]
        newList.append(1)
        newList.insert(0, 1)
        pascale.append(newList)
    return (pascale)
