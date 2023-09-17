import pygame
from Game import *

class board(object):
    def __init__(self):
        self.tmp = None
        self.board = [
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "]
        ]
        self.WIDTH = self.HEIGHT = 512
        self.SIZE = (self.WIDTH, self.HEIGHT)
        self.screen = pygame.display.set_mode(self.SIZE)
        self.WHITE = (255, 255, 255)
        self.BLACK = (200, 170, 128)
        self.HIGH = (174, 240, 89)
        self.SQUARE_SIZE = self.WIDTH // 8
        self.W_PAWN_IMAGE = pygame.image.load('Assets/wp.png')
        self.W_ROOK_IMAGE = pygame.image.load('Assets/wr.png')
        self.W_KNIGHT_IMAGE = pygame.image.load('Assets/wkn.png')
        self.W_BISHOP_IMAGE = pygame.image.load('Assets/wb.png')
        self.W_QUEEN_IMAGE = pygame.image.load('Assets/wq.png')
        self.W_KING_IMAGE = pygame.image.load('Assets/wk.png')
        self.B_PAWN_IMAGE = pygame.image.load('Assets/bp.png')
        self.B_ROOK_IMAGE = pygame.image.load('Assets/br.png')
        self.B_KNIGHT_IMAGE = pygame.image.load('Assets/bkn.png')
        self.B_BISHOP_IMAGE = pygame.image.load('Assets/bb.png')
        self.B_QUEEN_IMAGE = pygame.image.load('Assets/bq.png')
        self.B_KING_IMAGE = pygame.image.load('Assets/bk.png')
        self.move_sound = pygame.mixer.Sound("Assets/move-self.mp3")
        self.capture_sound = pygame.mixer.Sound("Assets/capture.mp3")
        pygame.display.set_caption("PyChess")
        pygame.display.set_icon(self.W_KNIGHT_IMAGE)

    def reset_board(self):
        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]

    def set(self, posx, posy, piece):
        self.board[posy][posx] = piece

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                x = col * self.SQUARE_SIZE
                y = row * self.SQUARE_SIZE
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.screen, self.WHITE, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
                else:
                    pygame.draw.rect(self.screen, self.BLACK, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))

    def draw_pieces(self):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece == "P":
                    self.screen.blit(self.W_PAWN_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece == "R":
                    self.screen.blit(self.W_ROOK_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece == "N":
                    self.screen.blit(self.W_KNIGHT_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece == "B":
                    self.screen.blit(self.W_BISHOP_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece == "Q":
                    self.screen.blit(self.W_QUEEN_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece == "K":
                    self.screen.blit(self.W_KING_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece == "p":
                    self.screen.blit(self.B_PAWN_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece == "r":
                    self.screen.blit(self.B_ROOK_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece == "n":
                    self.screen.blit(self.B_KNIGHT_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece == "b":
                    self.screen.blit(self.B_BISHOP_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece == "q":
                    self.screen.blit(self.B_QUEEN_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece == "k":
                    self.screen.blit(self.B_KING_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))

    @staticmethod
    def calc_mouse():
        import math as mt
        return [mt.trunc(int(pygame.mouse.get_pos()[0]) / 64), mt.trunc(int(pygame.mouse.get_pos()[1]) / 64)]

    def highlights(self, highlights):
        for pos in highlights:
            self.highlight(pos)

    def highlight(self, pos):
        pygame.draw.rect(self.screen, self.HIGH, (pos[0] * 64, pos[1] * 64, self.SQUARE_SIZE, self.SQUARE_SIZE), )

    def draw_mouse_piece(self, piece):
        if piece == "P":
            self.screen.blit(self.W_PAWN_IMAGE, ([pygame.mouse.get_pos()[0] - 32, pygame.mouse.get_pos()[1] - 32]))
        elif piece == "R":
            self.screen.blit(self.W_ROOK_IMAGE, ([pygame.mouse.get_pos()[0] - 32, pygame.mouse.get_pos()[1] - 32]))
        elif piece == "N":
            self.screen.blit(self.W_KNIGHT_IMAGE, ([pygame.mouse.get_pos()[0] - 32, pygame.mouse.get_pos()[1] - 32]))
        elif piece == "B":
            self.screen.blit(self.W_BISHOP_IMAGE, ([pygame.mouse.get_pos()[0] - 32, pygame.mouse.get_pos()[1] - 32]))
        elif piece == "Q":
            self.screen.blit(self.W_QUEEN_IMAGE, ([pygame.mouse.get_pos()[0] - 32, pygame.mouse.get_pos()[1] - 32]))
        elif piece == "K":
            self.screen.blit(self.W_KING_IMAGE, ([pygame.mouse.get_pos()[0] - 32, pygame.mouse.get_pos()[1] - 32]))
        elif piece == "p":
            self.screen.blit(self.B_PAWN_IMAGE, ([pygame.mouse.get_pos()[0] - 32, pygame.mouse.get_pos()[1] - 32]))
        elif piece == "r":
            self.screen.blit(self.B_ROOK_IMAGE, ([pygame.mouse.get_pos()[0] - 32, pygame.mouse.get_pos()[1] - 32]))
        elif piece == "n":
            self.screen.blit(self.B_KNIGHT_IMAGE, ([pygame.mouse.get_pos()[0] - 32, pygame.mouse.get_pos()[1] - 32]))
        elif piece == "b":
            self.screen.blit(self.B_BISHOP_IMAGE, ([pygame.mouse.get_pos()[0] - 32, pygame.mouse.get_pos()[1] - 32]))
        elif piece == "q":
            self.screen.blit(self.B_QUEEN_IMAGE, ([pygame.mouse.get_pos()[0] - 32, pygame.mouse.get_pos()[1] - 32]))
        elif piece == "k":
            self.screen.blit(self.B_KING_IMAGE, ([pygame.mouse.get_pos()[0] - 32, pygame.mouse.get_pos()[1] - 32]))

    def tick(self):
        self.draw_board()
        self.highlight(self.calc_mouse())
        self.draw_pieces()
        pygame.display.flip()
        if pygame.event.get(pygame.MOUSEBUTTONDOWN):
            mousex = self.calc_mouse()[0]
            mousey = self.calc_mouse()[1]
            piece = self.board[mousey][mousex]
            self.set(mousex, mousey, " ")
            holding = True
            while holding:
                self.draw_board()
                self.highlight(self.calc_mouse())
                self.draw_pieces()
                self.draw_mouse_piece(piece)
                pygame.display.flip()
                if pygame.event.get(pygame.MOUSEBUTTONUP):
                    mousex = self.calc_mouse()[0]
                    mousey = self.calc_mouse()[1]
                    if self.board[mousey][mousex] == " ":
                        pygame.mixer.Sound.play(self.move_sound)
                    else:
                        pygame.mixer.Sound.play(self.capture_sound)
                    self.set(mousex, mousey, piece)
                    holding = False
