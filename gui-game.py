import random
import pygame

board = [' ' for x in range(9)]

WIDTH, HEIGHT = 340, 340
WHITE = (255, 255, 255)
FPS = 30

#clock = pygame.time.Clock(FPS)

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

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

square1 = pygame.draw.rect(WIN, WHITE, (square_positions[0][0], square_positions[0][1], square_size[0], square_size[1]))
square2 = pygame.draw.rect(WIN, WHITE, (square_positions[1][0], square_positions[1][1], square_size[0], square_size[1]))
square3 = pygame.draw.rect(WIN, WHITE, (square_positions[2][0], square_positions[2][1], square_size[0], square_size[1]))
square4 = pygame.draw.rect(WIN, WHITE, (square_positions[3][0], square_positions[3][1], square_size[0], square_size[1]))
square5 = pygame.draw.rect(WIN, WHITE, (square_positions[4][0], square_positions[4][1], square_size[0], square_size[1]))
square6 = pygame.draw.rect(WIN, WHITE, (square_positions[5][0], square_positions[5][1], square_size[0], square_size[1]))
square7 = pygame.draw.rect(WIN, WHITE, (square_positions[6][0], square_positions[6][1], square_size[0], square_size[1]))
square8 = pygame.draw.rect(WIN, WHITE, (square_positions[7][0], square_positions[7][1], square_size[0], square_size[1]))
square9 = pygame.draw.rect(WIN, WHITE, (square_positions[8][0], square_positions[8][1], square_size[0], square_size[1]))

#text = font.render('X', 1, (0, 0, 0))
#WIN.blit(text, (10, 10))

def main():
    clock = pygame.time.Clock()
    #clock.tick()

    run = True

    while run:
        clock.tick(FPS)

        #pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                
                if square1.collidepoint(pos):
                    board[0] = 'X'

        draw()

        #pygame.display.update()

    pygame.quit()

def draw():
    #WIN.fill((0, 0, 0))
    for position, letter in enumerate(board):
        text = font.render(letter, 1, (0, 0, 0))
        WIN.blit(text, (square_positions[position][0] + 25, square_positions[position][1] + 20))
    pygame.display.update()

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