from src.tictactoe_mechanics import TictactoeGame, GameOverError
import pygame


def initialize_game():
    screen.fill("wheat3")
    update_top_bar_message("Tic Tac Toe")
    full_screen_message("Welcome to Tic Tac Toe!", 1000)
    create_empty_board()


def new_game():
    print("new game started")
    create_empty_board()
    update_top_bar_message("New game started. Press anywhere on the board to make the first move.")
    # initiate game
    global my_game
    my_game = TictactoeGame()


def create_empty_board():
    pygame.draw.rect(screen, "wheat3", pygame.Rect(0, top_of_board, width, height - top_of_board))
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


def update_top_bar_message(message):
    # empty top bar
    pygame.draw.rect(screen, "wheat4", pygame.Rect(0, 0, width, 100))
    pygame.draw.line(screen, "black", (0, 100), (width, 100), 5)
    # print text
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(message, True, "black")
    text_rect = text.get_rect(center=(width / 2, 50))
    screen.blit(text, text_rect)
    # update
    pygame.display.flip()


def full_screen_message(message, time):
    # empty background
    pygame.draw.rect(screen, "wheat3", pygame.Rect(0, top_of_board, width, height - top_of_board))
    pygame.draw.line(screen, "black", (0, 100), (width, 100), 5)
    # text
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(message, True, "black")
    text_rect = text.get_rect(center=(width / 2, height / 2))
    screen.blit(text, text_rect)
    # wait and update
    pygame.display.flip()
    pygame.time.wait(time)


def make_a_move(x, y):
    # determine what location on the board the user clicked
    col = int(x/200)
    row = int((y-100)/200)
    # advance the game
    symbol = my_game.next_to_move
    try:
        my_game.move(row, col)
    except ValueError:
        print("Seems like somebody already made a move on that field. Choose a different field.")
        return
    except GameOverError:
        print("Game over! You can't move anymore.")
        return
    # place a symbol on the board
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
    # line 1
    line1_start_x = 3 * margin + 200 * column
    line1_start_y = top_of_board + 3 * margin + 200 * row
    line1_end_x = 200 * column + 200 - 3 * margin
    line1_end_y = top_of_board + 200 * row + 200 - 3 * margin
    # line 2
    line2_start_x = 3 * margin + 200 * column
    line2_start_y = top_of_board + 200 * row + 200 - 3 * margin
    line2_end_x = 200 * column + 200 - 3 * margin
    line2_end_y = top_of_board + 3 * margin + 200 * row
    # draw
    pygame.draw.line(screen, "wheat4", (line1_start_x, line1_start_y), (line1_end_x, line1_end_y), 15)
    pygame.draw.line(screen, "wheat4", (line2_start_x, line2_start_y), (line2_end_x, line2_end_y), 15)


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
initialize_game()
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
        pygame.display.flip()
        pygame.time.wait(500)
        if my_game.winner == "Draw":
            full_screen_message("Game over! The game ended in a draw.", 1500)
        else:
            full_screen_message("{} won! Congratulations.".format(my_game.winner), 1500)
        full_screen_message("Starting new game...", 1000)
        new_game()
    pygame.display.flip()
