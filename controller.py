from model import MatrixModel
from view import print_matrix, print_help, get_command


def one_move(matrix: MatrixModel) -> None:
    '''One move'''
    command = get_command()
    if command == 'exit' or not matrix.move(command):
        raise KeyboardInterrupt
    print_matrix(matrix.matrix)

def init_game() -> MatrixModel:
    print_help()

    size = get_size()
    matrix = MatrixModel(size)

    print_matrix(matrix.matrix)
    return matrix


def get_size() -> int:
    '''Get size of matrix
       Return int(size) of matrix'''

    while True:
        size = input('Enter size of matrix from 4 to 8: ')
        if size.lower() == 'exit':
            raise KeyboardInterrupt
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
