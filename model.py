from copy import deepcopy
from random import choice

__all__ = [
    'MATRIX',
    'move',
    'search_free_positions',
    'set_two_in_random_position',
    'set_matrix',
    'set_two_in_start_matrix',
    ]


MATRIX = []


def set_matrix(size) -> list[list[int]]:
    '''Setting of matrix.
       Return matrix'''

    for _ in range(size):
        MATRIX.append([0] * size)


def set_two_in_start_matrix():
    '''set two in start matrix'''

    zeros = search_free_positions()
    set_two_in_random_position(zeros)


def search_free_positions() -> dict:
    '''Searching of all free positions in matrix'''

    zeros = {}

    for i in range(len(MATRIX)):
        row_zeros = []
        for j in range(len(MATRIX)):
            if MATRIX[i][j] == 0:
                row_zeros.append(j)
        if row_zeros:
            zeros[i] = row_zeros
    return zeros


def set_two_in_random_position(zeros: dict) -> None:
    '''Random selection of a position for a new "2".'''
    pos_i = choice([*zeros.keys()])
    pos_j = choice(zeros[pos_i])
    MATRIX[pos_i][pos_j] = 2


def move(command) -> bool:
    '''Start of moving matrix.
       Return True if matrix changed'''

    matrix_old = deepcopy(MATRIX)

    if command in 'aф':
        move_left(MATRIX)
    elif command in 'dв':
        move_right(MATRIX)
    elif command in 'wц':
        move_top()
    else:
        move_down()

    if MATRIX != matrix_old:
        return True


def move_left(matrix: list[list[int]]) -> None:
    '''Move and merge digits in matrix to left'''

    for i in range(len(matrix)):
        move_row_left(matrix[i])


def move_row_left(row: list[int]) -> None:
    '''Move and merge digits in row to left'''

    i = 0
    for _ in range(len(row) - 1):
        if row[i] * row[i + 1] == 0 or (row[i] and row[i] == row[i + 1]):
            row[i] += row[i + 1]
            row.pop(i + 1)
            row.append(0)
        else:
            i += 1


def move_right(matrix: list[list[int]]) -> None:
    '''Move and merge digits in matrix to right'''

    # Reverse matrix
    for i in range(len(matrix)):
        matrix[i].reverse()

    move_left(matrix)

    # Back reverse matrix
    for i in range(len(matrix)):
        matrix[i].reverse()


def move_top() -> None:
    '''Move and merge digits in matrix to top'''

    transposed_matrix = transpose_matrix()

    move_left(transposed_matrix)

    back_transpose_matrix(transposed_matrix)


def move_down() -> None:
    '''Move and merge digits in matrix to down'''

    transposed_matrix = transpose_matrix()

    move_right(transposed_matrix)

    back_transpose_matrix(transposed_matrix)


def transpose_matrix() -> list[list[int]]:
    '''Transpose matrix.
       Return new transposed matrix.'''

    transposed_matrix = [[0] * len(MATRIX) for _ in range(len(MATRIX))]

    for i in range(len(MATRIX)):
        for j in range(len(MATRIX)):
            transposed_matrix[j][i] = MATRIX[i][j]

    return transposed_matrix


def back_transpose_matrix(transposed_matrix: list[list[int]]) -> None:
    '''Back transpose matrix'''

    for i in range(len(MATRIX)):
        for j in range(len(MATRIX)):
            MATRIX[j][i] = transposed_matrix[i][j]
