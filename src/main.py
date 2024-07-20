from src.tictactoe_mechanics import TictactoeGame, GameOverError
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
    # determine what location on the board the user clicked
    col = int(x/200)
    row = int((y-100)/200)
    # advance the game
    try:
        symbol = my_game.next_to_move
        my_game.move(row, col)
    except ValueError:
        print("Seems like somebody already made a move on that field. Choose a different field.")
        return
    except GameOverError:
        print("Game over! You can't move anymore.")
        return
    draw_shape[symbol](row, col)
    print("move made")
    print("row: {}, column: {}".format(row, col))


def draw_circle(row, column):
    print("circle drawn")
    radius = (square_size / 2 - 2 * margin)
    circlex = 100 + 200 * column
    circley = top_of_board + 100 + 200 * row
    pygame.draw.circle(screen, "wheat4", (circlex, circley), radius, width = 10)


def draw_cross(row, column):
    print("cross drawn")
    # pygame.draw.line(screen, "black", (row, column), (column, row), 5)
    # pygame.draw.line(screen, "black", (row, column), (column, row), 5)


pygame.init()

# global settings for pygame
## only mouse clicks are registered
pygame.event.set_allowed(None)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
## screen size and caption
width = 600
height = 700
margin = 10
top_of_board = 100
square_size = 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic-Tac-Toe')
## define circle and cross
draw_shape = {
    1: draw_circle,
    -1: draw_cross
}


# start first game
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
