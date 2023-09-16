from Board import *

pygame.init()

chess = board()


def update_board():
    chess.drag_n_drop()
    pygame.display.flip()
    pass


running = True
while running:
    update_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pass
pygame.quit()
