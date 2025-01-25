from model import move, search_free_positions, set_two_in_random_position, set_matrix, set_two_in_start_matrix
from view import print_matrix, print_help, get_command


def run_game(matrix):
    '''Run game'''
    command = get_command()
    flag = move(matrix, command)
    if flag:
        zeros = search_free_positions(matrix)
        if zeros:
            set_two_in_random_position(zeros, matrix)
        else:
            print('Вы проиграли')
            raise KeyboardInterrupt

    print_matrix(matrix)


def configure_game():
    print_help()

    size = get_size()
    matrix = set_matrix(size)
    set_two_in_start_matrix(matrix)

    print_matrix(matrix)
    return matrix


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
