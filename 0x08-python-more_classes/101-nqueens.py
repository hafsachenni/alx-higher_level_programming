#!/usr/bin/python3
import sys


def init_board(n):
    """Initialize an NxN sized chessboad"""
    board = []
    [board.append([]) for a in range(n)]
    [row.append(' ') for a in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists"""
    solution = []
    for r in range(len(board)):
        for i in range(len(board)):
            if board[r][i] == "Q":
                solution.append([r, i])
                break
    return (solution)


def xout(board, row, col):
    for i in range(col + 1, len(board)):
        board[row][i] = "x"
    for i in range(col - 1, -1, -1):
        board[row][i] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    i = col + 1
    for r in range(row + 1, len(board)):
        if i >= len(board):
            break
        board[r][i] = "x"
        i += 1
    i = col - 1
    for r in range(row - 1, -1, -1):
        if i < 0:
            break
        board[r][i]
        i -= 1
    i = col + 1
    for r in range(row - 1, -1, -1):
        if i >= len(board):
            break
        board[r][i] = "x"
        i += 1
    i = col - 1
    for r in range(row + 1, len(board)):
        if i < 0:
            break
        board[r][i] = "x"
        i -= 1


def recursive_solve(board, row, queens, solutions):
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for i in range(len(board)):
        if board[row][i] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][i] = "Q"
            xout(tmp_board, row, i)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
