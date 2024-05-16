#!/usr/bin/python3
"""Prime Game"""


def decide(arr, i):
    """decide the winner"""
    turn = 0
    Ben = 0
    maria = 0
    if(len(arr) == 1):
        return "Ben"
    while (len(arr) > 0):
        val = arr[0]
        mul = 2
        if (turn % 2):
            Ben = Ben + 1
            while val * mul <= i:
                arr.remove(val * mul)
                mul = mul + 1
            arr.remove(val)
        else:
            maria = maria + 1
            while val * mul <= i:
                arr.remove(val * mul)
                mul = mul + 1
            arr.remove(val)
        turn = turn + 1
    if(Ben >= maria):
        return "Ben"
    else:
        return "Maria"


def isWinner(x, nums):
    """Prime Game"""
    Ben = 0
    maria = 0
    for i in nums:
        arr = [x for x in range(2, i + 1)]
        if(decide(arr, i) == "Ben"):
            Ben = Ben + 1
        else:
            maria = maria + 1
    if(Ben > maria):
        return "Ben"
    elif (maria > Ben):
        return "Maria"
    else:
        return None
