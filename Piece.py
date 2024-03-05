import pygame as pg


class Piece(object):
    def __init__(self, screen):
        self.screen = screen
        self.type = ""
        self.row = 0
        self.col = 0
        self.isWhite = True

    def row_col_to_index(self):
        index = ((self.row - 1) * 8) + self.col
        return index

    def draw_piece(self):
