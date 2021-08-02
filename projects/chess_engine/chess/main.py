class InvalidMove(Exception):
    pass

class InvalidPieceCharacteristic(Exception):
    pass

class Engine():
    def start():
        pass

class Piece():
    file = 0                               # between a and h
    rank = 0                               # between 1 and 8
    COLOR = 'No color'
    valid_files = [ord('a'), ord('b'), ord('c'), 
                        ord('d'), ord('e'), ord('f'),
                        ord('g'), ord('h')]
    valid_ranks = [1, 2, 3, 4, 5, 6, 7, 8]

    # Check the start position to decide which color a piece is
    
    def verify_file(self, file):
        if ord(file) in self.valid_files:
            return file
        else:
            return InvalidPieceCharacteristic(
                             """Non legal value for file given.
                                Expected a value between 'a' and 'h'.
                                Given file: {}""".format(file))
    
    def verify_rank(self, rank):
        if  rank in self.valid_ranks:
            return rank
        else:
            return InvalidPieceCharacteristic(
                             """Non legal value for rank given.
                                Expected a value between 1 and 8 respectively.
                                Given rank: {}""".format(rank))

    def verify_color(self, color):
        if color in ['white', 'black']:
            return color
        else:
            raise InvalidPieceCharacteristic(
                             """The color given is not a legal value. 
                                Expected 'white' or 'black' given {}""".format(color))

    def __init__(self):
        print ('You need to select an actual piece.')

    def location(self):
        return (self.file, self.rank)      # return a tuple ('a', '1')

    def verify_move(self):                     # An empty function to be inherited
        pass 

    def move(self, target):                     # Move the piece at the target square 
        if target in self.verify_move():
            self.file = target[0]
            self.rank = target[1]
            return (self.file, self.rank)
        else:
            raise InvalidMove('This is not a legal move')

class Pawn(Piece):
    
    def __init__(self, file, rank, color):
        self.file = self.verify_file(file)
        self.rank = self.verify_rank(rank)
        self.COLOR = self.verify_color(color)
    
    def rank_movement(self):
        valid_moves = []
        if self.COLOR == 'white':             # white movement
            if self.location()[1] == 2:          
                valid_moves.append(self.rank + 1)
                valid_moves.append(self.rank + 2)
                return valid_moves
            else:
                valid_moves.append(self.verify_rank(self.rank + 1))
                return valid_moves
        else:                            # black movement
            if self.location()[1] == 7:
                valid_moves.append(self.rank - 1)
                valid_moves.append(self.rank - 2)
                return valid_moves
            else:
                valid_moves.append(self.verify_rank(self.rank - 1))
                return valid_moves

    def file_movement(self):
        valid_moves = []
        valid_moves.append(self.file)
        return valid_moves

    def verify_move(self):
        valid_moves = []
        # get lists of valid moves for each characteristic
        valid_ranks = self.rank_movement()
        valid_files = self.file_movement()
        # build tuples with valid moves
        for rank in valid_ranks:
            for file in valid_files:
                move = [file, rank]
                valid_moves.append(tuple(move))
        # return a list with the tuples - (file, rank)
        print (valid_moves)
        return valid_moves

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Rook(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass

class Board():
    pass



pawn = Pawn(file = 'a', rank = 2, color = 'white')
print (pawn.COLOR, pawn.file, pawn.rank)
move = ('a', 4)
pawn.move(move)
print ("Successful move!")
move = ('b', 5)
pawn.move(move)