game_on = True

matrix = [
        [' ', '|', ' ', '|', ' '],
        ['--', '', '--', '', '--'],
        [' ', '|', ' ', '|', ' '],
        ['--', '', '--', '', '--'],
        [' ', '|', ' ', '|', ' '],
    ]


def check_win(matrix, symbol):
    if matrix[0][0] == symbol and matrix[0][2] == symbol and matrix[0][4] == symbol:
        if symbol == 'X':
            print('Player 1 is the winner!!! Congrats')
            print('Better luck next time Player 2')
        else:
            print('Player 2 is the winner!!! Congrats')
            print('Better luck next time Player 1')
        return 1

    if matrix[2][0] == symbol and matrix[2][2] == symbol and matrix[2][4] == symbol:
        if symbol == 'X':
            print('Player 1 is the winner!!! Congrats')
            print('Better luck next time Player 2')
        else:
            print('Player 2 is the winner!!! Congrats')
            print('Better luck next time Player 1')
        return 1

    if matrix[4][0] == symbol and matrix[4][2] == symbol and matrix[4][4] == symbol:
        if symbol == 'X':
            print('Player 1 is the winner!!! Congrats')
            print('Better luck next time Player 2')
        else:
            print('Player 2 is the winner!!! Congrats')
            print('Better luck next time Player 1')
        return 1

    if matrix[0][0] == symbol and matrix[2][0] == symbol and matrix[4][0] == symbol:
        if symbol == 'X':
            print('Player 1 is the winner!!! Congrats')
            print('Better luck next time Player 2')
        else:
            print('Player 2 is the winner!!! Congrats')
            print('Better luck next time Player 1')
        return 1

    if matrix[2][2] == symbol and matrix[0][2] == symbol and matrix[4][2] == symbol:
        if symbol == 'X':
            print('Player 1 is the winner!!! Congrats')
            print('Better luck next time Player 2')
        else:
            print('Player 2 is the winner!!! Congrats')
            print('Better luck next time Player 1')
        return 1

    if matrix[0][4] == symbol and matrix[2][4] == symbol and matrix[4][4] == symbol:
        if symbol == 'X':
            print('Player 1 is the winner!!! Congrats')
            print('Better luck next time Player 2')
        else:
            print('Player 2 is the winner!!! Congrats')
            print('Better luck next time Player 1')
        return 1

    if matrix[0][0] == symbol and matrix[2][2] == symbol and matrix[4][4] == symbol:
        if symbol == 'X':
            print('Player 1 is the winner!!! Congrats')
            print('Better luck next time Player 2')
        else:
            print('Player 2 is the winner!!! Congrats')
            print('Better luck next time Player 1')
        return 1

    if matrix[4][0] == symbol and matrix[2][2] == symbol and matrix[0][4] == symbol:
        if symbol == 'X':
            print('Player 1 is the winner!!! Congrats')
            print('Better luck next time Player 2')
        else:
            print('Player 2 is the winner!!! Congrats')
            print('Better luck next time Player 1')
        return 1


def player1(matrix):
    count = 0
    print('Player 1')
    number = input('Enter a position between 1 to 9 - ')
    number = int(number)

    if number > 9 or number < 1:
        print("Invalid input")
        player1(matrix)
    else:
        symbol = "X"
        result = switch_demo(number, symbol)
        if result == 2:
            player1(matrix)


def player2(matrix):
    print('Player 2')
    number = input('Enter a position between 1 to 9 - ')
    number = int(number)

    if number > 9 or number < 1:
        print("Invalid input --- outofbounds")
        player2(matrix)
    else:
        symbol = "O"
        result = switch_demo(number, symbol)
        if result == 3:
            player2(matrix)


def switch_demo(number, symbol):
    if number == 1:
        if matrix[0][0] == "X" or matrix[0][0] == "O":
            print('Place already occupied -- Try another Position')
            if symbol == 'X':
                return 2
            else:
                return 3

        else:
            matrix[0][0] = symbol
    if number == 2:
        if matrix[0][2] == "X" or matrix[0][2] == "O":
            print('Place already occupied -- Try another Position')
            if symbol == 'X':
                player1(matrix)
            else:
                player2(matrix)
        else:
            matrix[0][2] = symbol
    if number == 3:
        if matrix[0][4] == "X" or matrix[0][4] == "O":
            print('Place already occupied -- Try another Position')
            if symbol == 'X':
                player1(matrix)
            else:
                player2(matrix)
        else:
            matrix[0][4] = symbol
    if number == 4:
        if matrix[2][0] == "X" or matrix[2][0] == "O":
            print('Place already occupied -- Try another Position')
            if symbol == 'X':
                player1(matrix)
            else:
                player2(matrix)
        else:
            matrix[2][0] = symbol
    if number == 5:
        if matrix[2][2] == "X" or matrix[2][2] == "O":
            print('Place already occupied -- Try another Position')
            if symbol == 'X':
                player1(matrix)
            else:
                player2(matrix)
        else:
            matrix[2][2] = symbol
    if number == 6:
        if matrix[2][4] == "X" or matrix[2][4] == "O":
            print('Place already occupied -- Try another Position')
            if symbol == 'X':
                player1(matrix)
            else:
                player2(matrix)
        else:
            matrix[2][4] = symbol
    if number == 7:
        if matrix[4][0] == "X" or matrix[4][0] == "O":
            print('Place already occupied -- Try another Position')
            if symbol == 'X':
                player1(matrix)
            else:
                player2(matrix)
        else:
            matrix[4][0] = symbol
    if number == 8:
        if matrix[4][2] == "X" or matrix[4][2] == "O":
            print('Place already occupied -- Try another Position')
            if symbol == 'X':
                player1(matrix)
            else:
                player2(matrix)
        else:
            matrix[4][2] = symbol
    if number == 9:
        if matrix[4][4] == "X" or matrix[4][4] == "O":
            print('Place already occupied -- Try another Position')
            if symbol == 'X':
                player1(matrix)
            else:
                player2(matrix)
        else:
            matrix[4][4] = symbol

    return matrix


def game_board(matrix):

    for row in matrix:
        for col in row:
            print(col, end=' ')
        print()


def check_fill(matrix):

    if not matrix[0][0] == ' ' and not matrix[0][2] == ' ' and not matrix[0][4] == ' ' and not matrix[2][0] == ' ' and \
            not matrix[2][2] == ' ' and not matrix[2][4] == ' ' and not matrix[4][0] == ' ' and \
            not matrix[4][2] == ' ' and not matrix[4][4] == ' ':
        print()
        print("**---Draw---**")
        exit()


print('Welcome to TicTacToe Game!!!')
print('Player 1 will use "X"')
print('Player 2 will use "O"')

start = input('Do you want to start the game -- y for yes, n for no  : ')
if start == 'y':
    print()
    print('--LetsStart--')
    print()
    print()
    game_board(matrix)
if start == 'n':
    exit()


while game_on:

    check_fill(matrix)
    player1(matrix)
    game_board(matrix)
    num = check_win(matrix, 'X')
    if num == 1:
        break
    check_fill(matrix)
    player2(matrix)
    game_board(matrix)
    num = check_win(matrix, 'O')
    if num == 1:
        break
    check_fill(matrix)


















