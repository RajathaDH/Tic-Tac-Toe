board = [' ' for x in range(9)]

def main():
    print('Game started')

    game_end = False

    # run game until board is full
    while not game_end:
        player_turn()
        print_board(board)

        # end game if no free spaces in board
        if board.count(' ') < 1:
            game_end = True

    print('Game ended')

def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def player_turn():
    made_move = False

    while not made_move:
        try:
            player_move = int(input('Enter a position (1-9) '))
            if player_move < 1 or player_move > 9:
                print('Enter a valid position')
            else:
                player_position = player_move - 1 # player index in board
                if board[player_position] != ' ':
                    print('Position is already taken')
                else:
                    board[player_position] = 'X'
                    made_move = True
        except:
            print('Enter a valid number')

if __name__ == '__main__':
    main()