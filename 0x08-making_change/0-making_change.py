#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """Making Change"""
    if(total <= 0):
        return 0
    coins.sort(reverse=True)
    i = 0
    sum = 0
    num = 0
    while(i < len(coins)):
        while(sum + coins[i] <= total):
            sum = sum + coins[i]
            num = num + 1
        i = i + 1
    if (sum == total):
        return num
    return -1
