#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    Ben = 0
    maria = 0
    for i in nums:
        arr = [x for x in range(2, i + 1)]
        turn = 0
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
