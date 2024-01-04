#!/usr/bin/python3
"""Implementation of the N-queens puzzle.

This script solves the problem of arranging N queens on an NxN chessboard such that no two queens threaten each other.

Usage example:
    $ ./101-nqueens.py N

Where N is an integer that is 4 or greater.

Attributes:
    board (list): Represents the chessboard as a list of lists.
    solutions (list): Contains the solutions as lists of lists.

Each solution is formatted as [[r, c], [r, c], ...] where `r` and `c` indicate the row and column for placing a queen.
"""
import sys


def create_board(n):
    """Create an `n`x`n` chessboard initialized with empty spaces."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def deepcopy_board(board):
    """Create a deep copy of the chessboard."""
    if isinstance(board, list):
        return [deepcopy_board(row) for row in board]
    return board


def find_solution(board):
    """Generate a solution from the current board state."""
    solution = []
    for row_index, row in enumerate(board):
        for col_index, cell in enumerate(row):
            if cell == "Q":
                solution.append([row_index, col_index])
                break
    return solution


def mark_danger_zones(board, row, col):
    """Mark positions where queens cannot be placed after putting a queen at (row, col)."""
    n = len(board)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in directions:
        r, c = row, col
        while 0 <= r < n and 0 <= c < n:
            board[r][c] = 'x'
            r += dr
            c += dc


def solve_n_queens(board, row, num_queens, solutions):
    """Recursively solve the N-queens problem."""
    if num_queens == len(board):
        solutions.append(find_solution(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == ' ':
            new_board = deepcopy_board(board)
            new_board[row][col] = 'Q'
            mark_danger_zones(new_board, row, col)
            solve_n_queens(new_board, row + 1, num_queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    n = sys.argv[1]
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = create_board(n)
    all_solutions = solve_n_queens(chessboard, 0, 0, [])
    for solution in all_solutions:
        print(solution)

