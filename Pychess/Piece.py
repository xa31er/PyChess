import pygame as pg

class PieceTypeNotValidError(Exception):
    """Raised when trying to assign an invalid piece type to a piece"""
    def __init__(self, piece_type):
        self.value = piece_type
    def __str__(self):
        return(repr(self.value))

class Piece(object):
    def __init__(self, piece_type : str = "No type Specified!"):
        # Pygame Init
        pg.init()

        # Valid Pieces
        self.pieces = [
            "P", "p", "r", "N", "n", "B", "b", "K", "k", "Q", "q",
        ]

        # Piece Sprites
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

        # Sounds
        self.move_sound = pg.mixer.Sound("Assets/move-self.mp3")
        self.capture_sound = pg.mixer.Sound("Assets/capture.mp3")
        
        # Piece variables
        try:
            assert self.is_valid_type(piece_type)
        except AssertionError:
            raise PieceTypeNotValidError(piece_type)

        self.row = 0
        self.col = 0
        
        # Set piece color 
        if piece_type[0].upper() == piece_type:
            self.isWhite = True
        else:
            self.isWhite = False
        

    def row_col_to_index(self):
        index = ((self.row - 1) * 8) + self.col
        return index

    def draw_piece(self):
        self.screen.blit(self.images[self.type], (self.col * self.square_size, self.row * self.square_size))

    def set_type(self, new_type):
        self.type = new_type
        if new_type[0].upper() == new_type:
            self.isWhite = True
        else:
            self.isWhite = False

    def get_type(self):
        return self.type[0]
    
    def is_valid_type(self, type_to_check : str):
        if type_to_check in self.pieces:
            return True
        else:
            return False

if __name__ == "__main__":
    test_piece = Piece("p")
