'''
2048 - console game.
User can choice size of matrix from 4 to 8.
Type "exit" to exit
'''

import random
from copy import deepcopy


def run_game():
    '''Run game loop'''

    while True:
        flag = move()
        if flag:
            zeros = search_free_positions()
            if zeros:
                set_two_in_random_position(zeros)
            else:
                print('Вы проиграли')
                raise KeyboardInterrupt

        print_matrix()


def set_matrix() -> list[list[int]]:
    '''Setting of matrix.
       Return matrix'''

    size = get_size()
    matrix = [[0] * size for i in range(size)]

    return matrix


def set_two_in_start_matrix():
    '''set two in start matrix'''

    zeros = search_free_positions()
    set_two_in_random_position(zeros)


def get_size() -> int:
    '''Get size of matrix
       Return int(size) of matrix'''

    while True:
        size = input('Enter size of matrix from 4 to 8: ')
        if size.lower() == 'exit':
            print()
            print('Bye!')
            exit()
        elif not size:
            continue
        elif len(size) != 1:
            continue
        elif not size.isdigit():
            continue
        elif size not in '45678':
            continue
        else:
            break
    return int(size)


def search_free_positions() -> dict:
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


def set_two_in_random_position(zeros: dict) -> None:
    '''Random selection of a position for a new "2".'''

    pos_i = random.choice([*zeros.keys()])
    pos_j = random.choice(zeros[pos_i])
    matrix[pos_i][pos_j] = 2


def print_matrix():
    '''Print matrix to console'''

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                print('.', end=' ')
            else:
                print(matrix[i][j], end=' ')
        print()


def move() -> bool:
    '''Start of moving matrix.
       Return True if matrix changed'''

    matrix_old = deepcopy(matrix)

    command = get_command()

    if command in 'aф':
        move_left(matrix)
    elif command in 'dв':
        move_right(matrix)
    elif command in 'wц':
        move_top()
    else:
        move_down()

    if matrix != matrix_old:
        return True


def get_command() -> str:
    '''Get of command
       Return command'''

    while True:
        command = input('Enter the command: ').lower()
        cmd_validation(command)
        if cmd_validation(command):
            break

    return command


def cmd_validation(command: str) -> bool:
    '''Command validation'''

    if command.lower() == 'exit':
        print()
        print('Bye!')
        exit()
    elif not command:
        return False
    elif not command.isalpha():
        return False
    elif len(command) != 1:
        return False
    elif command not in 'wasdцфыв':
        return False
    else:
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

    transposed_matrix = [[0] * len(matrix) for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


def back_transpose_matrix(transposed_matrix: list[list[int]]) -> None:
    '''Back transpose matrix'''

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[j][i] = transposed_matrix[i][j]


if __name__ == '__main__':
    try:
        print('Commands:')
        print("'W' or 'w' - Up")
        print("'S' or 's' - Down")
        print("'A' or 'a' - Left")
        print("'D' or 'd' - Right")

        matrix = set_matrix()
        set_two_in_start_matrix()

        print_matrix()

        run_game()

    except KeyboardInterrupt:
        print()
        print('Bye!')
        exit()
