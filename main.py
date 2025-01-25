from controller import run_game, configure_game


def main():
    '''Run game loop'''
    try:
        matrix = configure_game()
        while True:
            run_game(matrix)

    except KeyboardInterrupt:
        print()
        print('Bye!')
        exit()


if __name__ == '__main__':
    main()
