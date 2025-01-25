import random
from copy import deepcopy


def set_matrix(size) -> list[list[int]]:
    '''Setting of matrix.
       Return matrix'''

    matrix = [[0] * size for i in range(size)]

    return matrix


def set_two_in_start_matrix(matrix):
    '''set two in start matrix'''

    zeros = search_free_positions(matrix)
    set_two_in_random_position(zeros, matrix)


def search_free_positions(matrix) -> dict:
    '''Searching of all free positions in matrix'''

    zeros = {}

    for i in range(len(matrix)):
        row_zeros = []
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                row_zeros.append(j)
        if row_zeros:
            zeros[i] = row_zeros
    return zeros


def set_two_in_random_position(zeros: dict, matrix) -> None:
    '''Random selection of a position for a new "2".'''

    pos_i = random.choice([*zeros.keys()])
    pos_j = random.choice(zeros[pos_i])
    matrix[pos_i][pos_j] = 2


def move(matrix, command) -> bool:
    '''Start of moving matrix.
       Return True if matrix changed'''

    matrix_old = deepcopy(matrix)

    if command in 'aф':
        move_left(matrix)
    elif command in 'dв':
        move_right(matrix)
    elif command in 'wц':
        move_top(matrix)
    else:
        move_down(matrix)

    if matrix != matrix_old:
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


def move_top(matrix) -> None:
    '''Move and merge digits in matrix to top'''

    transposed_matrix = transpose_matrix(matrix)

    move_left(transposed_matrix)

    back_transpose_matrix(matrix, transposed_matrix)


def move_down(matrix) -> None:
    '''Move and merge digits in matrix to down'''

    transposed_matrix = transpose_matrix(matrix)

    move_right(transposed_matrix)

    back_transpose_matrix(matrix, transposed_matrix)


def transpose_matrix(matrix) -> list[list[int]]:
    '''Transpose matrix.
       Return new transposed matrix.'''

    transposed_matrix = [[0] * len(matrix) for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


def back_transpose_matrix(matrix, transposed_matrix: list[list[int]]) -> None:
    '''Back transpose matrix'''

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[j][i] = transposed_matrix[i][j]
