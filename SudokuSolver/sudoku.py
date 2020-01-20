import random
from typing import List, Tuple, Optional
import copy


def generate_board() -> List[List[int]]:

    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    count = 0
    min_board_values = random.randint(17, 40)

    for i in range(9):
        for j in range(9):
            value = random.randint(1, 9)
            if count == min_board_values:
                value = 0
                break
            if valid(board, value, (i, j)):
                board[i][j] = value
                count += 1
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for k in range(1, 10):
                    if valid(board, k, (i, j)):
                        board[i][j] = k
                        board_copy = copy.deepcopy(board)
                        if solve(board):
                            return board_copy


# Backtracking algorithm
def solve(board: List[List[int]]):  # Recursion

    find = find_empty(board)
    if not find:
        return True  # Base Case
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False


def valid(board: List[List[int]], num: int, pos: Tuple[int, int]) -> bool:

    # Check row for duplicate num
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column for duplicate num
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 square for duplicate num
    box_x = pos[1] // 3  # Columns 0, 1, 2 in the first box, etc.
    box_y = pos[0] // 3  # Rows 0, 1, 2 in the first box, etc.

    # Loop through each box to check for duplicate num

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(board: List[List[int]]) -> None:

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board: List[List[int]]) -> Optional[Tuple[int, int]]:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # row, col
    return None


