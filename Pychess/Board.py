from Piece import *


class Board(object):
    def __init__(self):
        self.tmp = None
        self.WIDTH = self.HEIGHT = 512
        self.SIZE = (self.WIDTH, self.HEIGHT)
        self.screen = pg.display.set_mode(self.SIZE)
        self.WHITE = (255, 255, 255)
        self.BLACK = (200, 170, 128)
        self.HIGH = (174, 240, 89)
        self.SQUARE_SIZE = self.WIDTH // 8
        self.W_PAWN_IMAGE = pg.image.load('Assets/wp.png')
        self.W_ROOK_IMAGE = pg.image.load('Assets/wr.png')
        self.W_KNIGHT_IMAGE = pg.image.load('Assets/wkn.png')
        self.W_BISHOP_IMAGE = pg.image.load('Assets/wb.png')
        self.W_QUEEN_IMAGE = pg.image.load('Assets/wq.png')
        self.W_KING_IMAGE = pg.image.load('Assets/wk.png')
        self.B_PAWN_IMAGE = pg.image.load('Assets/bp.png')
        self.B_ROOK_IMAGE = pg.image.load('Assets/br.png')
        self.B_KNIGHT_IMAGE = pg.image.load('Assets/bkn.png')
        self.B_BISHOP_IMAGE = pg.image.load('Assets/bb.png')
        self.B_QUEEN_IMAGE = pg.image.load('Assets/bq.png')
        self.B_KING_IMAGE = pg.image.load('Assets/bk.png')
        self.move_sound = pg.mixer.Sound("Assets/move-self.mp3")
        self.capture_sound = pg.mixer.Sound("Assets/capture.mp3")
        pg.display.set_caption("PyChess")
        pg.display.set_icon(self.W_KNIGHT_IMAGE)
        self.start_pos = [
            "r", "n", "b", "q", "k", "b", "n", "r",
            "p", "p", "p", "p", "p", "p", "p", "p",
            " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ",
            "P", "P", "P", "P", "P", "P", "P", "P",
            "R", "N", "B", "Q", "K", "B", "N", "R"
        ]
        self.board = [
        ]
        for i in range(64):
            self.board.append(Piece(self.screen,self.SQUARE_SIZE,""))
    
    def set(self, posx, posy, piece):
        self.board[posy][posx] = piece

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                x = col * self.SQUARE_SIZE
                y = row * self.SQUARE_SIZE
                if (row + col) % 2 == 0:
                    pg.draw.rect(self.screen, self.WHITE, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
                else:
                    pg.draw.rect(self.screen, self.BLACK, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))

    def draw_pieces(self):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece.getType() == "P":
                    self.screen.blit(self.W_PAWN_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece.getType() == "R":
                    self.screen.blit(self.W_ROOK_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece.getType() == "N":
                    self.screen.blit(self.W_KNIGHT_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece.getType() == "B":
                    self.screen.blit(self.W_BISHOP_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece.getType() == "Q":
                    self.screen.blit(self.W_QUEEN_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece.getType() == "K":
                    self.screen.blit(self.W_KING_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece.getType() == "p":
                    self.screen.blit(self.B_PAWN_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece.getType() == "r":
                    self.screen.blit(self.B_ROOK_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece.getType() == "n":
                    self.screen.blit(self.B_KNIGHT_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece.getType() == "b":
                    self.screen.blit(self.B_BISHOP_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece.getType() == "q":
                    self.screen.blit(self.B_QUEEN_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))
                elif piece.getType() == "k":
                    self.screen.blit(self.B_KING_IMAGE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE))

    @staticmethod
    def calc_mouse():
        import math as mt  
        return [mt.trunc(int(pg.mouse.get_pos()[0]) / 64), mt.trunc(int(pg.mouse.get_pos()[1]) / 64)]

    def highlight(self):
        pg.draw.rect(self.screen, self.HIGH,
                     (self.calc_mouse()[0] * 64, self.calc_mouse()[1] * 64, self.SQUARE_SIZE, self.SQUARE_SIZE), )

    def draw_mouse_piece(self, piece):
        if piece == "P":
            self.screen.blit(self.W_PAWN_IMAGE, ([pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] - 32]))
        elif piece == "R":
            self.screen.blit(self.W_ROOK_IMAGE, ([pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] - 32]))
        elif piece == "N":
            self.screen.blit(self.W_KNIGHT_IMAGE, ([pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] - 32]))
        elif piece == "B":
            self.screen.blit(self.W_BISHOP_IMAGE, ([pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] - 32]))
        elif piece == "Q":
            self.screen.blit(self.W_QUEEN_IMAGE, ([pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] - 32]))
        elif piece == "K":
            self.screen.blit(self.W_KING_IMAGE, ([pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] - 32]))
        elif piece == "p":
            self.screen.blit(self.B_PAWN_IMAGE, ([pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] - 32]))
        elif piece == "r":
            self.screen.blit(self.B_ROOK_IMAGE, ([pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] - 32]))
        elif piece == "n":
            self.screen.blit(self.B_KNIGHT_IMAGE, ([pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] - 32]))
        elif piece == "b":
            self.screen.blit(self.B_BISHOP_IMAGE, ([pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] - 32]))
        elif piece == "q":
            self.screen.blit(self.B_QUEEN_IMAGE, ([pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] - 32]))
        elif piece == "k":
            self.screen.blit(self.B_KING_IMAGE, ([pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] - 32]))

    def tick(self):
        self.draw_board()
        self.highlight()
        self.draw_pieces()
        pg.display.flip()
        if pg.event.get(pg.MOUSEBUTTONDOWN):
            mousex = self.calc_mouse()[0]
            mousey = self.calc_mouse()[1]
            piece = self.board[mousey][mousex]
            self.set(mousex, mousey, " ")
            holding = True
            while holding:
                self.draw_board()
                self.highlight()
                self.draw_pieces()
                self.draw_mouse_piece(piece)
                pg.display.flip()
                if pg.event.get(pg.MOUSEBUTTONUP):
                    mousex = self.calc_mouse()[0]
                    mousey = self.calc_mouse()[1]
                    if self.board[mousey][mousex] == " ":
                        pg.mixer.Sound.play(self.move_sound)
                        print("empty")
                    else:
                        pg.mixer.Sound.play(self.capture_sound)
                        print("full")
                    self.set(mousex, mousey, piece)
                    holding = False

    def reset_board(self):
        i = 0
        for piece in self.board:
            piece.setType(self.start_pos[i])
            i += 1
    
    # def calc_moves(self, x, y, piece):
    #   if piece == "p" and y = 2
