def print_help() -> None:
    print('Commands:')
    print("'W' or 'w' - Up")
    print("'S' or 's' - Down")
    print("'A' or 'a' - Left")
    print("'D' or 'd' - Right")


def print_matrix(matrix: list[list]) -> None:
    '''Print matrix to console'''

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                print('.', end=' ')
            else:
                print(matrix[i][j], end=' ')
        print()


def get_command() -> str:
    '''Validation and return command: up, down, left, right, exit'''

    while True:
        input_command = input('Enter the command: ').lower()
        command = cmd_validation(input_command)
        if command:
            break

    return command


def cmd_validation(command: str) -> bool | str:
    '''Command validation'''

    if command == 'exit':
        return command
    elif not command:
        return False
    elif not command.isalpha():
        return False
    elif len(command) != 1:
        return False
    elif command in 'wц':
        return 'up'
    elif command in 'aф':
        return 'left'
    elif command in 'sы':
        return 'down'
    elif command in 'dв':
        return 'right'
