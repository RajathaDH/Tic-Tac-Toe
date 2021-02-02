import random
import pygame

WIDTH, HEIGHT = 340, 340
WHITE = (255, 255, 255)

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 30

board = [' ' for x in range(9)]

pygame.display.set_caption('Tic-Tac-Toe')
font = pygame.font.SysFont('sans-serif', 100)

square_size = (100, 100)
square_positions = [
    (10, 10),
    (120, 10),
    (230, 10),
    (10, 120),
    (120, 120),
    (230, 120),
    (10, 230),
    (120, 230),
    (230, 230)
]

def main():
    clock = pygame.time.Clock()

    run = True

    game_end = False

    player_move = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if player_move:
                    clicked_position = event.pos
                    player_turn(clicked_position)
                    player_move = False

        if not game_end:
            draw()
            if check_winner(board):
                WIN.fill((255, 255, 255))
                text = font.render('WIN', 1, (0, 0, 0))
                WIN.blit(text, (10, 10))
                game_end = True

            if not player_move and not game_end:
                computer_move = computer_turn()
                board[computer_move] = 'O'
                player_move = True
                if check_winner(board):
                    WIN.fill((255, 255, 255))
                    text = font.render('LOSE', 1, (0, 0, 0))
                    WIN.blit(text, (10, 10))
                    game_end = True

        if board.count(' ') < 1:
            WIN.fill((255, 255, 255))
            text = font.render('Tie Game', 1, (0, 0, 0))
            WIN.blit(text, (10, 10))
            game_end = True

        pygame.display.update()

    pygame.quit()

def draw():
    WIN.fill((0, 0, 0))

    # draw squares
    for position in square_positions:
        pygame.draw.rect(WIN, WHITE, (position[0], position[1], square_size[0], square_size[1]))
    
    # draw letters
    for position, letter in enumerate(board):
        colour = (0, 0, 0) if letter == 'X' else (255, 0, 0)
        text = font.render(letter, 1, colour)
        WIN.blit(text, (square_positions[position][0] + 25, square_positions[position][1] + 20))
    
def player_turn(position):
    x = position[0]
    y = position[1]

    for index, square_position in enumerate(square_positions):
        if x >= square_position[0] and x <= (square_position[0] + square_size[0]) and y >= square_position[1] and y <= (square_position[1] + square_size[1]):
            board[index] = 'X'
            break

def check_winner(board):
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
    return move

if __name__ == '__main__':
    main()