# Example file showing a circle moving on screen
import sys

import pygame


def new_game():
    # fill the screen
    screen.fill("wheat3")
    print("new game started")
    # write a welcome text
    # create boxes to make a board

def make_a_move():
    print("move made")
    # pygame.Rect.collidepoint

# pygame setup
pygame.init()
# global settings for pygame
pygame.event.set_allowed(None)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic-Tac-Toe')
new_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    # user closed window and quit game
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:    # used clicked on something in the window
            pos = pygame.mouse.get_pos()
            # make a move
            make_a_move()
    pygame.display.flip()
