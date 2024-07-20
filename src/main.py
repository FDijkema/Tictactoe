"""Run this script to play a game of Tic-tac-toe in a visual interface"""

from src.tictactoe_mechanics import TictactoeGame, GameOverError
import pygame


def initialize_and_welcome_players():
    """fill the screen with background colour and write a welcome message for the players"""
    screen.fill("wheat3")
    update_top_bar_message("Welcome to Tic Tac Toe!")
    create_empty_board()
    pygame.display.flip()
    pygame.time.wait(2000)


def new_game():
    """empty the game board and start a new game"""
    create_empty_board()
    update_top_bar_message("")
    # initiate game
    global my_game
    my_game = TictactoeGame()
    update_top_bar_message("Next to move: {}".format(text_symbol[my_game.next_to_move]))


def create_empty_board():
    """"fill the lower half of the screen with an empty tictactoe board"""
    pygame.draw.rect(screen, "wheat3", pygame.Rect(0, top_of_board, width, height - top_of_board))
    pygame.draw.line(screen, "black", (0, 100), (width, 100), 5)
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
    """"write a message on the top part of the screen"""
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
    """empty the lower part of the screen and write a message in the center"""
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
    """advance the game with one move and place a symbol on the board"""
    # determine what location on the board the user clicked
    col = int(x/200)
    row = int((y-100)/200)
    # advance the game
    symbol = my_game.next_to_move
    try:
        my_game.move(row, col)
    except ValueError:
        pygame.time.wait(200)
        update_top_bar_message("Invalid move. Try again.")
        return
    except GameOverError:
        pygame.time.wait(200)
        update_top_bar_message("Game Over. You can't move anymore.")
        return
    # place a symbol on the board
    draw_shape[symbol](row, col)
    pygame.display.flip()
    pygame.time.wait(200)
    update_top_bar_message("Next to move: {}".format(text_symbol[my_game.next_to_move]))


def draw_circle(row, column):
    """draw a circle on the board at the indicated location"""
    radius = (square_size / 2 - 2 * margin)
    circlex = 100 + 200 * column
    circley = top_of_board + 100 + 200 * row
    pygame.draw.circle(screen, "wheat4", (circlex, circley), radius, width = 10)


def draw_cross(row, column):
    """draw a cross on the board at the indicated location"""
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


# start pygame so the attributes can be used
pygame.init()
# global settings for pygame events
pygame.event.set_allowed(None)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
# screen size and caption
width = 600
height = 700
margin = 10
top_of_board = 100
square_size = 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic-Tac-Toe')
# define which player is circle and which one is cross
draw_shape = {
    1: draw_circle,
    -1: draw_cross
}
text_symbol = {
    1: "O",
    -1: "X"
}

# start the first game
initialize_and_welcome_players()
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
            full_screen_message("It's a draw!", 2000)
        else:
            full_screen_message("Congratulations {}! You win!".format(my_game.winner), 2000)
        full_screen_message("Starting new game...", 1000)
        new_game()
    pygame.display.flip()
