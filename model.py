from copy import deepcopy
from random import choice


class MatrixModel:
    '''Method .move() - one move in matrix.
    Attribute matrix - get the matrix'''
    def __init__(self, size: int):
        self._matrix = [[0] * size for _ in range(size)]
        self._size = size
        self._zeros = {}
        self._commands = set()

        self._set_two_in_random_position()

    @property
    def matrix(self):
        return self._matrix

    def _search_free_positions(self) -> dict:
        '''Searching of all free positions in matrix'''
        self._zeros = {}

        for i in range(self._size):
            row_zeros = []
            for j in range(self._size):
                if self._matrix[i][j] == 0:
                    row_zeros.append(j)
            if row_zeros:
                self._zeros[i] = row_zeros

    def _set_two_in_random_position(self) -> None:
        '''Random selection of a position for a new "2".'''
        self._search_free_positions()


        pos_i = choice([*self._zeros.keys()])
        pos_j = choice(self._zeros[pos_i])
        self._matrix[pos_i][pos_j] = 2

    def move(self, command) -> bool:
        '''Start of moving matrix.
           Return True if matrix changed or there is a place to move'''

        old_matrix = deepcopy(self._matrix)

        match command:
            case 'left':
                self._move_left(self._matrix)
            case 'right':
                self._move_right(self._matrix)
            case 'up':
                self._move_top()
            case 'down':
                self._move_down()
        
        return self._is_succcess_move(old_matrix, command)

    def _is_succcess_move(self, old_matrix, command) -> bool:
        '''Is it successfull move or not'''
        if self._matrix != old_matrix:
            self._set_two_in_random_position()
            self._commands.clear()
        else:
            self._commands.add(command)
            if len(self._commands) > 3:
                return False
        return True

    def _move_left(self, matrix: list[list[int]]) -> None:
        '''Move and merge digits in matrix to left'''

        for i in range(len(matrix)):
            self._move_row_left(matrix[i])

    def _move_row_left(self, row: list[int]) -> None:
        '''Move and merge digits in row to left'''

        i = 0
        for _ in range(len(row) - 1):
            if row[i] * row[i + 1] == 0 or (row[i] and row[i] == row[i + 1]):
                row[i] += row[i + 1]
                row.pop(i + 1)
                row.append(0)
            else:
                i += 1

    def _move_right(self, matrix: list[list[int]]) -> None:
        '''Move and merge digits in matrix to right'''

        # Reverse matrix
        for i in range(len(matrix)):
            matrix[i].reverse()

        self._move_left(matrix)

        # Back reverse matrix
        for i in range(len(matrix)):
            matrix[i].reverse()

    def _move_top(self) -> None:
        '''Move and merge digits in matrix to top'''
        transposed_matrix = self._transpose_matrix()
        self._move_left(transposed_matrix)
        self._back_transpose_matrix(transposed_matrix)

    def _move_down(self) -> None:
        '''Move and merge digits in matrix to down'''
        transposed_matrix = self._transpose_matrix()
        self._move_right(transposed_matrix)
        self._back_transpose_matrix(transposed_matrix)

    def _transpose_matrix(self) -> list[list[int]]:
        '''Transpose matrix.
        Return new transposed matrix.'''
        transposed_matrix = [[0] * self._size for _ in range(self._size)]

        for i in range(self._size):
            for j in range(self._size):
                transposed_matrix[j][i] = self._matrix[i][j]

        return transposed_matrix


    def _back_transpose_matrix(self, transposed_matrix: list[list[int]]) -> None:
        '''Back transpose matrix'''
        for i in range(self._size):
            for j in range(self._size):
                self._matrix[j][i] = transposed_matrix[i][j]
