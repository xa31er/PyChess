import pygame as pg


class Piece(object):
    def __init__(self, screen, square_size, piece_type):
        self.images = {
            "P": pg.image.load('Assets/wp.png'),
            "p": pg.image.load('Assets/bp.png'),
            "R": pg.image.load('Assets/wr.png'),
            "r": pg.image.load('Assets/br.png'),
            "N": pg.image.load('Assets/wkn.png'),
            "n": pg.image.load('Assets/bkn.png'),
            "B": pg.image.load('Assets/wb.png'),
            "b": pg.image.load('Assets/bb.png'),
            "K": pg.image.load('Assets/wk.png'),
            "k": pg.image.load('Assets/bk.png'),
            "Q": pg.image.load('Assets/wq.png'),
            "q": pg.image.load('Assets/bq.png')
        }
        self.move_sound = pg.mixer.Sound("Assets/move-self.mp3")
        self.capture_sound = pg.mixer.Sound("Assets/capture.mp3")
        self.screen = screen
        self.type = piece_type
        self.row = 0
        self.col = 0
        self.isWhite = True
        self.square_size = square_size

    def row_col_to_index(self):
        index = ((self.row - 1) * 8) + self.col
        return index

    def draw_piece(self):
        self.screen.blit(self.images[self.type], (self.col * self.square_size, self.row * self.square_size))

    def setType(self, new_type):
        self.type = new_type
        if new_type[0].upper() == new_type:
            self.isWhite = True
        else:
            self.isWhite = False

    def getType(self):
        return self.type[0]