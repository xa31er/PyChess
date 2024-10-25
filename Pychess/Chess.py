from Board import *
import pygame
pygame.init()

chess = Board()

chess.reset_board()

def update_board():
    chess.tick()
    pass


running = True
while running:
    update_board()
    if pygame.event.get(pygame.QUIT):
        running = False
    pass
pygame.quit()
