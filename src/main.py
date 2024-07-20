from src.tictactoe_mechanics import TictactoeGame
import pygame


def new_game():
    # fill the screen
    screen.fill("wheat3")
    print("new game started")

    # screen layout
    pygame.draw.rect(screen, "wheat4", pygame.Rect(0, 0, width, 100))
    pygame.draw.line(screen, "black", (0, 100), (width, 100), 5)
    # board
    pygame.draw.line(screen, "wheat4",
                     (margin, top_of_board + square_size),
                     (width - margin, top_of_board + square_size), 10)
    pygame.draw.line(screen, "wheat4",
                     (margin, top_of_board + 2 * square_size),
                     (width - margin, top_of_board + 2 * square_size), 10)
    pygame.draw.line(screen, "wheat4",
                     (square_size, top_of_board + margin),
                     (square_size, height - margin), 10)
    pygame.draw.line(screen, "wheat4",
                     (2 * square_size, top_of_board + margin),
                     (2 * square_size, height - margin), 10)

    # write a welcome text
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Welcome to Tic-tac-toe', True, "black")
    text_rect = text.get_rect(center=(width / 2, 50))
    screen.blit(text, text_rect)

    # initiate game
    global my_game
    my_game = TictactoeGame()


def make_a_move(x, y):
    col = int(x/200)
    row = int((y-100)/200)
    my_game.move(row, col)
    print("move made")
    print("row: {}, column: {}".format(row, col))


# pygame setup
pygame.init()
# global settings for pygame
pygame.event.set_allowed(None)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)

width = 600
height = 700
margin = 10
top_of_board = 100
square_size = 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic-Tac-Toe')
new_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    # user closed window and quit game
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:    # user clicked on something in the window
            x, y = pygame.mouse.get_pos()
            if y > 100:    # user clicked on the board
                make_a_move(x, y)
            else:
                pass    # user clicked on something else
    # declare winner and ask to restart
    if my_game.game_over:
        print("Game over.")
        new_game()
    pygame.display.flip()
