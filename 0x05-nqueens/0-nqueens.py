#!/usr/bin/python3
"""N Queens module"""
import sys


def main():
    """n queens func"""
    if (len(sys.argv) != 2):
        print('Usage: nqueens N')
        sys.exit(1)
    if (not(sys.argv[1].isdigit())):
        print('N must be a number\n')
        sys.exit(1)
    if (int(sys.argv[1]) < 4):
        print('N must be at least 4\n')
        sys.exit(1)


if __name__ == '__main__':
    main()
