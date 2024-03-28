#!/usr/bin/python3
"""solve queen problem"""
import sys


def is_safe(b, row, col, n):
    """Check if there is a queen in the same column"""
    for i in range(row):
        if b[i] == col or b[i] == col + row - i or b[i] == col - row + i:
            return False
    return True


def solve_nqueens(n):
    """solve queen problem"""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def backtrack(row, board):
        if row == n:
            print(board)
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1, board)

    backtrack(0, [-1] * n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
