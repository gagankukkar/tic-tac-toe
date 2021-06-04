def board_printer(board_array):
    print('\t \t | \t \t | \t \t')
    print(f'\t {board_array[7]} \t | \t {board_array[8]} \t | \t {board_array[9]} \t')
    print('\t \t | \t \t | \t \t')
    print('---------+-------+--------')

    print('\t \t | \t \t | \t \t')
    print(f'\t {board_array[4]} \t | \t {board_array[5]} \t | \t {board_array[6]} \t')
    print('\t \t | \t \t | \t \t')
    print('---------+-------+--------')

    print('\t \t | \t \t | \t \t')
    print(f'\t {board_array[1]} \t | \t {board_array[2]} \t | \t {board_array[3]} \t')
    print('\t \t | \t \t | \t \t')


def turn_input(x_or_o, player):
    while True:
        try:
            spot = int(input(f'Enter {x_or_o} location {player} : '))
            if 1 <= spot <= 9:
                if board[spot] == '':
                    board[spot] = x_or_o
                    return spot
                else:
                    print('This spot has already been taken! Pick another spot.')
            else:
                print('Value must be between 1 to 9!')
        except ValueError:
            print('Not a valid input!')


def check_win(moves):
    winning_combos = ([1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [3,5,7], [1,5,9])
    for combo in winning_combos:
        if all(spot in moves for spot in combo):
            return True


def score_printer(track_score_obj):
    if track_score_obj['games_played'] > 0:
        print('--------------------------')
        print('\t\tScoreboard')
        print(f'Games played: {track_score_obj["games_played"]}')
        print(f'{player1} score: {track_score_obj[player1]}')
        print(f'{player2} score: {track_score_obj[player2]}')
        print('--------------------------\n')


board_demo = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print('Welcome to Tic Tac Toe!')

player1 = input('Player 1 (X), enter your name: ')
player2 = input('Player 2 (O), enter your name: ')

while player1 == player2:
    print('Players must have different names!')
    player2 = input('Player 2 (O), enter your name: ')

track_score = {
    'games_played': 0,
    player1: 0,
    player2: 0
}

print('Play your turn by entering a number location on the numpad.')

again = 'y'

while again == 'y' or again == 'Y':
    board = []
    for n in range(10):
        board.append('')

    board_printer(board_demo)

    track_moves = {
        player1: [],
        player2: []
    }

    for n in range(9):
        if n % 2 == 0:
            current_turn = turn_input('X', player1)
            track_moves[player1].append(current_turn)

        else:
            current_turn = turn_input('O', player2)
            track_moves[player2].append(current_turn)

        board_printer(board)

        if n < 4:
            continue

        elif check_win(track_moves[player1]):
            track_score[player1] += 1
            print(f'{player1} wins!')
            break

        elif check_win(track_moves[player2]):
            track_score[player2] += 1
            print(f'{player2} wins!')
            break

        elif n == 8:
            print('Tie game!')

    track_score['games_played'] += 1

    print('Play again? (y/n)')
    again = input('')

    score_printer(track_score)

    player_switch = player2
    player2 = player1
    player1 = player_switch