#!/usr/bin/python3
"""Solving N queens challenge"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]

    Args:
        board (list): The current state of the board.
        row (int): The row to check for safety.
        col (int): The column to check for safety.
        n (int): The size of the board.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n, solutions):
    """
    Recursive function to solve the N-Queens problem.

    Args:
        board (list): The current state of the board.
        row (int): The current row being considered.
        n (int): The size of the board.
        solutions (list): A list to store all the solutions found.
    """
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)


def print_solutions(n):
    """
    Print all solutions for the N-Queens problem.

    Args:
        n (str): The size of the board.
    """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    print_solutions(sys.argv[1])
