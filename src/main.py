# Example file showing a circle moving on screen
import sys

import pygame


def new_game():
    # fill the screen
    screen.fill("wheat3")
    print("new game started")
    # screen layout
    text_box = pygame.Rect(width, 100, 0,0)
    pygame.draw.rect(screen, "wheat4", pygame.Rect(0, 0, width, 100))
    # write a welcome text
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Welcome to Tic-tac-toe', True, "black")
    text_rect = text.get_rect(midtop=(width / 2, margin))
    screen.blit(text, text_rect)
    # create boxes to make a board

def make_a_move():
    print("move made")
    # pygame.Rect.collidepoint

# pygame setup
pygame.init()
# global settings for pygame
pygame.event.set_allowed(None)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)

width = 600
height = 700
margin = 10
screen = pygame.display.set_mode((width, height))
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
