def print_help():
    print('Commands:')
    print("'W' or 'w' - Up")
    print("'S' or 's' - Down")
    print("'A' or 'a' - Left")
    print("'D' or 'd' - Right")


def print_matrix(matrix):
    '''Print matrix to console'''

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                print('.', end=' ')
            else:
                print(matrix[i][j], end=' ')
        print()


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
