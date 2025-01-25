from controller import run_game, configure_game


def main():
    '''Run game loop'''
    try:
        configure_game()
        while True:
            run_game()

    except KeyboardInterrupt:
        print()
        print('Bye!')
        exit()


if __name__ == '__main__':
    main()
