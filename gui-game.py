import random
import pygame

board = [' ' for x in range(9)]

WIDTH, HEIGHT = 340, 340

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

square1 = pygame.draw.rect(WIN, (255, 255, 255), (10, 10, 100, 100))
square2 = pygame.draw.rect(WIN, (255, 255, 255), (120, 10, 100, 100))
square3 = pygame.draw.rect(WIN, (255, 255, 255), (230, 10, 100, 100))
square4 = pygame.draw.rect(WIN, (255, 255, 255), (10, 120, 100, 100))
square5 = pygame.draw.rect(WIN, (255, 255, 255), (120, 120, 100, 100))
square6 = pygame.draw.rect(WIN, (255, 255, 255), (230, 120, 100, 100))
square7 = pygame.draw.rect(WIN, (255, 255, 255), (10, 230, 100, 100))
square8 = pygame.draw.rect(WIN, (255, 255, 255), (120, 230, 100, 100))
square9 = pygame.draw.rect(WIN, (255, 255, 255), (230, 230, 100, 100))

def main():
    run = True

    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

"""def check_winner(board):
    # rows
    if ((board[0] == board[1] == board[2] != ' ') or
        (board[3] == board[4] == board[5] != ' ') or
        (board[6] == board[7] == board[8] != ' ')):
        return True

    # columns
    if ((board[0] == board[3] == board[6] != ' ') or
        (board[1] == board[4] == board[7] != ' ') or
        (board[2] == board[5] == board[8] != ' ')):
        return True

    # diagonals
    if ((board[0] == board[4] == board[8] != ' ') or
        (board[2] == board[4] == board[6] != ' ')):
        return True

    return False

def computer_turn():
    available_moves = [pos for pos, value in enumerate(board) if value == ' ']
    move = -1

    # check if computer can win by placing an O and return that position (win)
    for i in available_moves:
        new_board = board[:]
        new_board[i] = 'O'
        if check_winner(new_board):
            move = i
            return move

    # check if player will win next turn by placing an X and return that position (block player from winning next turn)
    for i in available_moves:
        new_board = board[:]
        new_board[i] = 'X'
        if check_winner(new_board):
            move = i
            return move

    # return an available corner
    avalable_corners = []
    for i in available_moves:
        if i in [0, 2, 6, 8]:
            avalable_corners.append(i)
    if len(avalable_corners) > 0:
        random_index = random.randrange(0, len(avalable_corners))
        move = avalable_corners[random_index]
        return move
    
    # return center position if available
    if 4 in available_moves:
        move = 4
        return move

    # return an available edge
    avalable_edges = []
    for i in available_moves:
        if i in [1, 3, 5, 7]:
            avalable_edges.append(i)
    if len(avalable_edges) > 0:
        random_index = random.randrange(0, len(avalable_edges))
        move = avalable_edges[random_index]
        return move

    # return initial move value
    return move"""

if __name__ == '__main__':
    main()