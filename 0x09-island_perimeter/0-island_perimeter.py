#!/usr/bin/python3
"""Island Perimeter """


def calcPerim(i, j, grid):
    """calculate perimeter"""
    perimeter = 0
    length = len(grid)
    rowLen = len(grid[i])
    if ((i > 0 and grid[i - 1][j] == 0) or (i == 0)):
        perimeter = perimeter + 1
    if ((i < length - 1 and grid[i + 1][j] == 0) or (i == length - 1)):
        perimeter = perimeter + 1
    if ((j > 0 and grid[i][j - 1] == 0) or (j == 0)):
        perimeter = perimeter + 1
    if ((j < rowLen - 1 and grid[i][j + 1] == 0) or (j == rowLen - 1)):
        perimeter = perimeter + 1
    return perimeter


def island_perimeter(grid):
    """Island Perimeter """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter = perimeter + calcPerim(i, j, grid)
    return perimeter
