#from movement import *
#from chess.custom_errors.errors import *
from pieces.movement import *
from custom_errors.errors import *

class Piece():
    file = 0                               # between a and h
    rank = 0                               # between 1 and 8 COLOR = 'No color'
    valid_files = [ord('a'), ord('b'), ord('c'), 
                   ord('d'), ord('e'), ord('f'),
                   ord('g'), ord('h')]
    valid_ranks = [1, 2, 3, 4, 5, 6, 7, 8]

    # Check the start position to decide which color a piece is
    
    def verify_file(self, file):
        if ord(file) in self.valid_files:
            return file
        else:
            raise InvalidFile("""\n
                Non legal value for file given.\n
                Expected a value between 'a' and 'h'.\n
                Given file: {}""".format(file))
    
    def verify_rank(self, rank):
        if  rank in self.valid_ranks:
            return rank
        else:
            raise InvalidRank("""\n
                Non legal value for rank given.\n
                Expected a value between 1 and 8.\n
                Given rank: {}""".format(rank))

    def verify_color(self, color):
        if color in ['white', 'black']:
            return color
        else:
            raise InvalidColor("""\n
                The color given is not a legal value.\n
                Expected 'white' or 'black' given {}""".format(color))

    def __init__(self):
        print ('You need to select an actual piece.')

    def location(self):
        return (self.file, self.rank)           # return a tuple ('a', 1)

    def verify_move(self):                      # An empty function to be inherited
        pass 

    def move(self, target):                     # Move the piece at the target square  
        if isinstance(target, str):
            coord_tuple = (target[0], int(target[1]))
        elif isinstance(target, tuple):
            coord_tuple = target
        else: 
            raise InvalidTargetDeclaration("""
                The coordinates of the raget 
                square are not defined correctly
                """)
        if coord_tuple in self.verify_move():
            self.file = target[0]
            self.rank = target[1]
            return (self.file, self.rank)
        else:
             raise InvalidMove('You have specified an illegal move')

class Pawn(Piece):
    
    def __init__(self, file, rank, color):
        self.file = self.verify_file(file)
        self.rank = self.verify_rank(rank)
        self.COLOR = self.verify_color(color)
    
    def verify_move(self):
        valid_moves = []
        for move in pawn_movement(self.location(), self.COLOR):
            try:
                self.verify_file(move[0])
                self.verify_rank(move[1])
            except InvalidRank:
                raise InvalidMove ("You have specified an illegal move")
            except InvalidFile:
                raise InvalidMove ("You have specified an illegal move")
            valid_moves.append(move)
        return valid_moves

class Knight(Piece):
    
    def __init__(self, file, rank, color):
        self.file = self.verify_file(file)
        self.rank = self.verify_rank(rank)
        self.COLOR = self.verify_color(color)

    def verify_move(self):
        valid_moves = []
        for move in knight_movement(self.location()):
            try:
                self.verify_file(move[0])
                self.verify_rank(move[1])
            except InvalidRank:
                raise InvalidMove ("You have specified an illegal move")
            except InvalidFile:
                raise InvalidMove ("You have specified an illegal move")
            valid_moves.append(move)
        return valid_moves

class Bishop(Piece):
    
    def __init__(self, file, rank, color):
        self.file = self.verify_file(file)
        self.rank = self.verify_rank(rank)
        self.COLOR = self.verify_color(color)
    
    def verify_move(self):
        valid_moves = []
        for move in bishop_movement(self.location()):
            try:
                self.verify_file(move[0])
                self.verify_rank(move[1])
            except InvalidRank:
                raise InvalidMove ("You have specified an illegal move")
            except InvalidFile:
                raise InvalidMove ("You have specified an illegal move")
            valid_moves.append(move)
        return valid_moves

class Rook(Piece):
    
    def __init__(self, file, rank, color):
        self.file = self.verify_file(file)
        self.rank = self.verify_rank(rank)
        self.COLOR = self.verify_color(color)

    def verify_move(self):
        valid_moves = []
        for move in rook_movement(self.location()):
            try:
                self.verify_file(move[0])
                self.verify_rank(move[1])
            except InvalidRank:
                raise InvalidMove ("You have specified an illegal move")
            except InvalidFile:
                raise InvalidMove ("You have specified an illegal move")
            valid_moves.append(move)
        return valid_moves

class Queen(Piece):
    
    def __init__(self, file, rank, color):
        self.file = self.verify_file(file)
        self.rank = self.verify_rank(rank)
        self.COLOR = self.verify_color(color)
    
    def verify_move(self):
        valid_moves = []
        for move in bishop_movement(self.location()):
            try:
                self.verify_file(move[0])
                self.verify_rank(move[1])
            except InvalidRank:
                raise InvalidMove ("You have specified an illegal move")
            except InvalidFile:
                raise InvalidMove ("You have specified an illegal move")
            valid_moves.append(move)
        for move in rook_movement(self.location()):
            try:
                self.verify_file(move[0])
                self.verify_rank(move[1])
            except InvalidRank:
                raise InvalidMove ("You have specified an illegal move")
            except InvalidFile:
                raise InvalidMove ("You have specified an illegal move")
            valid_moves.append(move)
        return valid_moves 

class King(Piece):
    
    def __init__(self, file, rank, color):
        self.file = self.verify_file(file)
        self.rank = self.verify_rank(rank)
        self.COLOR = self.verify_color(color)
    
    def verify_move(self):
        valid_moves = []
        for move in king_movement(self.location()):
            try:
                self.verify_file(move[0])
                self.verify_rank(move[1])
            except InvalidRank:
                raise InvalidMove ("You have specified an illegal move")
            except InvalidFile:
                raise InvalidMove ("You have specified an illegal move")
            valid_moves.append(move)
        return valid_moves

if __name__ == '__main__':
    pass
#    knight = Knight('b', 1, 'white')
#    print (knight.verify_move())

#    bishop = Bishop('f', 4, 'white')
#    print (bishop.verify_move())

#    rook = Rook  ('a', 1, 'white')
#    print (rook.verify_move())
#    print (rook.move('a8'))
#    queen = Queen('f', 4, 'white')
#    print (queen.verify_move())

#    king = King('f', 4, 'white')
#    print (king.verify_move())
