#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_queens(board, col, n):
    if col == n:
        print([[i, board[i]] for i in range(n)])
        return
    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve_queens(board, col + 1, n)

def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [-1] * n
    solve_queens(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

