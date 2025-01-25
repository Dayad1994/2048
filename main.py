from controller import one_move, init_game


def main():
    '''Run game loop'''
    try:
        matrix = init_game()
        while True:
            one_move(matrix)
    except KeyboardInterrupt:
        print()
        print('Bye!')
        exit()


if __name__ == '__main__':
    main()
