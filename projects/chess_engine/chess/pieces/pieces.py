"""
Module defining all pieces for the game of chess.
"""
#from chess.custom_errors.errors import *
from pieces.movement import *
#from custom_errors.errors import *

class Piece():
    '''
    An abstract class used for defining common
    functions that are used by the pieces.
    '''

    # Common values
    file = 0                               # between a and h
    rank = 0                               # between 1 and 8 _color = 'No color'
    _color = None

    # Verification values
    valid_files = [ord('a'), ord('b'), ord('c'), 
                   ord('d'), ord('e'), ord('f'),
                   ord('g'), ord('h')]
    valid_ranks = [1, 2, 3, 4, 5, 6, 7, 8]
    
    def location(self):
        '''
        Returns the location of the object
        '''
        return (self.file, self.rank)           # return a tuple ('a', 1)
    
    def __init__(self, file, rank, color):
        '''
        Initialize an object.
        '''
        self.file = self.verify_file(file)
        self.rank = self.verify_rank(rank)
        self._color = self.verify_color(color)

    # Validation
    def verify_file(self, file):
        '''
        Check if a given file is within the valid range
        '''
        if ord(file) in self.valid_files:
            return file
        else:
            raise InvalidFile("""\n
                Non legal value for file given.\n
                Expected a value between 'a' and 'h'.\n
                Given file: {}""".format(file))
    
    def verify_rank(self, rank):
        '''
        Check if a given rank is within the valid range
        '''
        if  rank in self.valid_ranks:
            return rank
        else:
            raise InvalidRank("""\n
                Non legal value for rank given.\n
                Expected a value between 1 and 8.\n
                Given rank: {}""".format(rank))

    def verify_color(self, color):
        '''
        Check if a the color of the object is either white or black
        '''
        if color in ['white', 'black']:
            return color
        else:
            raise InvalidColor("""\n
                The color given is not a legal value.\n
                Expected 'white' or 'black' given {}""".format(color))
    
    def verify_move(self):
        '''
        Returns a list with all valid locations for the object to be moved.
        '''
        pass 

    # Movement
    def move(self, target):
        '''
        The function changes the current values of self.rank and self.file.

        Args:
            target: A tuple or string representing the target coordinates to 
                    to move the object to.

        Errors:
            InvalidTargetDeclaration: Raised when the target value does not
                    meet the expected criteria.
            InvalidMove: Raised when the coordinates specified in the target 
                    argument are not valid.
        '''
        if isinstance(target, str):
            coord_tuple = (target[0], int(target[1]))
        elif isinstance(target, tuple):
            coord_tuple = target
        else: 
            raise InvalidTargetDeclaration(
                """ The coordinates of the target 
                square are not defined correctly
                """)
        if coord_tuple in self.verify_move():
            self.file = target[0]
            self.rank = target[1]
            return (self.file, self.rank)
        else:
             raise InvalidMove('You have specified an illegal move')
    
    #========== BISHOP & QUEEN movement ==========#
    def left_down(self, loc):
        moves = []
        file = loc[0]
        rank = loc[1]
        while ord(file) in self.valid_files and rank in self.valid_ranks:
            move = (file, rank)
            file = chr(ord(file) - 1)
            rank -= 1
            moves.append(move)
        moves = [move for move in moves if 0 not in move]
        return moves
    
    def left_up(self, loc):
        moves = []
        file = loc[0]
        rank = loc[1]
        while ord(file) in self.valid_files and rank in self.valid_ranks:
            move = (file, rank)
            file = chr(ord(file) - 1)
            rank += 1
            moves.append(move)
        moves = [move for move in moves if 0 not in move]
        return moves
    
    def right_up(self, loc):
        moves = []
        file = loc[0]
        rank = loc[1]
        while ord(file) in self.valid_files and rank in self.valid_ranks:
            move = (file, rank)
            file = chr(ord(file) + 1)
            rank += 1
            moves.append(move)
        moves = [move for move in moves if 0 not in move]
        return moves
    
    def right_down(self, loc):
        moves = []
        file = loc[0]
        rank = loc[1]
        while ord(file) in self.valid_files and rank in self.valid_ranks:
            move = (file, rank)
            file = chr(ord(file) + 1)
            rank -= 1
            moves.append(move)
        moves = [move for move in moves if 0 not in move]
        return moves
    
    def bishop_movement(self, loc):
        moves = []
        for move in self.left_up(self, loc):
            moves.append(move)
        for move in self.left_down(self, loc):
            moves.append(move)
        for move in self.right_up(self, loc):
            moves.append(move)
        for move in self.right_down(self, loc):
            moves.append(move)
        moves = list(set(moves))
        moves.remove(self, loc)
        return moves
    
    #========== ROOK & QUEEN movement ==========#
    def left(self, loc):
        moves = []
        file = loc[0]
        rank = loc[1]
        while ord(file) in self.valid_files:
            move = (file, rank)
            file = chr(ord(file) - 1)
            moves.append(move)
        return moves
    
    def right(self, loc):
        moves = []
        file = loc[0]
        rank = loc[1]
        while ord(file) in self.valid_files:
            move = (file, rank)
            file = chr(ord(file) + 1)
            moves.append(move)
        return moves
    
    def up(self, loc):
        moves = []
        file = loc[0]
        rank = loc[1]
        while rank in self.valid_ranks:
            move = (file, rank)
            rank += 1
            moves.append(move)
        return moves
    
    def down(self, loc):
        moves = []
        file = loc[0]
        rank = loc[1]
        while rank in self.valid_ranks:
            move = (file, rank)
            rank -= 1
            moves.append(move)
        return moves
    
    def rook_movement(self, loc):
        moves = []
        for move in self.left(self, loc):
            moves.append(move)
        for move in self.down(self, loc):
            moves.append(move)
        for move in self.up(self, loc):
            moves.append(move)
        for move in self.right(self, loc):
            moves.append(move)
        moves = list(set(moves))
        moves.remove(self, loc)
        return moves
    

class Pawn(Piece):
    
    #========== PAWN movement ==========#
    def pawn_rank_movement(self, loc, color):
        moves = []
        file = loc[0]
        rank = loc[1]
        if color == 'white':             # white movement
            if rank == 2:
                moves.append((file, rank + 1))
                moves.append((file, rank + 2))
            elif rank + 1 in valid_ranks:
                moves.append((file, rank + 1))
        else:                            # black movement
            if rank == 7:
                moves.append((file, rank - 1))
                moves.append((file, rank - 2))
            elif rank - 1 in valid_ranks:
                moves.append((file, rank - 1))
        return moves
    
    def pawn_file_movement(self, loc):
        moves = []
        file = loc[0]
        rank = loc[1]
        # if (check for takes):
        #     moves.append(chr(ord(file) +- 1) , rank)
        # NOTE This method needs to be called from the board
        return moves
    
    def pawn_movement(self, loc, color):
        moves = []
        for move in self.pawn_rank_movement(loc, color):
            moves.append(move)
        for move in pawn_file_movement(self, loc):
            moves.append(move)
        return moves

    def verify_move(self):
        valid_moves = []
        for move in self.pawn_movement(self.location(), self._color):
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

    #========== KNIGHT movement ==========#
    def front_back_moves(self, loc):
        moves = []
        file = loc[0]
        rank = loc[1]
        if rank + 2 in self.valid_ranks: rank_up = rank + 2
        else: rank_up = None
        if rank - 2 in self.valid_ranks: rank_down = rank - 2
        else: rank_down = None
        if ord(file) + 1 in self.valid_files: file_right = chr(ord(file) + 1)
        else: file_right = None
        if ord(file) - 1 in self.valid_files: file_left = chr(ord(file) - 1)
        else: file_left = None
    
        moves.append((file_left, rank_up))
        moves.append((file_right, rank_up))
        moves.append((file_left, rank_down))
        moves.append((file_right, rank_down))
        moves = [move for move in moves if move[0] != None and move[1] != None]
        return moves
    
    def left_right_moves(self, loc):
        moves = []
        file = loc[0]
        rank = loc[1]
        # The None values help prevent Unbound Local Errors
        if rank + 1 in self.valid_ranks: rank_up = rank + 1
        else: rank_up = None
        if rank - 1 in self.valid_ranks: rank_down = rank - 1
        else: rank_down = None
        if ord(file) + 2 in self.valid_files: file_right = chr(ord(file) + 2)
        else: file_right = None
        if ord(file) - 2 in self.valid_files: file_left = chr(ord(file) - 2)
        else: file_left = None
    
        moves.append((file_left, rank_up))
        moves.append((file_right, rank_up))
        moves.append((file_left, rank_down))
        moves.append((file_right, rank_down))
        moves = [move for move in moves if move[0] != None and move[1] != None]
        return moves
    
    def knight_movement(self, loc):
        moves = []
        for move in self.front_back_moves(self, loc):
            moves.append(move)
        for move in self.left_right_moves(self, loc):
            moves.append(move)
        return moves
    
    def verify_move(self):
        valid_moves = []
        for move in self.knight_movement(self.location()):
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
    
    def verify_move(self):
        valid_moves = []
        for move in self.bishop_movement(self.location()):
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

    def verify_move(self):
        valid_moves = []
        for move in self.rook_movement(self.location()):
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
    
    def verify_move(self):
        valid_moves = []
        for move in self.bishop_movement(self.location()):
            try:
                self.verify_file(move[0])
                self.verify_rank(move[1])
            except InvalidRank:
                raise InvalidMove ("You have specified an illegal move")
            except InvalidFile:
                raise InvalidMove ("You have specified an illegal move")
            valid_moves.append(move)
        for move in self.rook_movement(self.location()):
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
    
    #========== KING movement ==========#
    def king_movement(self, loc):
        moves = []
        file = loc[0]
        rank = loc[1]
        if ord(file) + 1 in self.valid_files and rank + 1 in self.valid_ranks:
            moves.append((chr(ord(file)+1), rank))
            moves.append((chr(ord(file)+1), rank+1))
            moves.append((chr(ord(file)), rank+1))
        if ord(file) - 1 in valid_files and rank - 1 in valid_ranks:
            moves.append((chr(ord(file)-1), rank))
            moves.append((chr(ord(file)-1), rank-1))
            moves.append((chr(ord(file)), rank-1))
        if ord(file) - 1 in valid_files and rank + 1 in valid_ranks:
            moves.append((chr(ord(file)-1), rank+1))
        if ord(file) + 1 in valid_files and rank - 1 in valid_ranks:
            moves.append((chr(ord(file)+1), rank-1))
        return moves
    
    def verify_move(self):
        valid_moves = []
        for move in self.king_movement(self.location()):
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
#    pass
    knight = Knight('b', 1, 'white')
    print (knight.verify_move())

    bishop = Bishop('f', 4, 'white')
    print (bishop.verify_move())

    rook = Rook  ('a', 1, 'white')
    print (rook.verify_move())
    print (rook.move('a8'))
    
    queen = Queen('f', 4, 'white')
    print (queen.verify_move())

    king = King('f', 4, 'white')
    print (king.verify_move())
