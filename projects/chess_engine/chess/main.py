# Structure
# class Engine
# class Piece:
# |_ class Pawn
# |_ class Knight
# |_ class Bishop
# |_ class Rook
# |_ class Queen
# |_ class King
# class Board

# Functions

# class Engine:
#   - start()       - start a new game with all needed pieces, intiate a new board 
#   - start_pos()   - start from a given position - useful for puzzles

# class Piece:
#   *file          - the x coordinates of the object (between a and h)
#   *rank          - the y coordinates of the object (between 1 and 8)
#   *COLOR          - enum value that shows a piece's color
#   - location()    - get the location of the piece; returns the coordinates
# of the piece
#   - check_move()  - check for legal moves; returns the coordinates of the 
# legal moves
#   - move()        - change the coordinates based on legal moves

# class Board:
#   *ID             - identification number of the board - make it a hash value
# to experiment with hashes?
#   *pieces         - create all pieces as objects and ues the variables as a way
# to communicate with them
#   - read_chess()  - extract all information from chess notations (remember to
# to turn all elements of the list in strings - security and failure)
#   - game_state()  - get the current location of all pieces in the game.
#   - king_check()  - check if any of the kings are in check; return True or False
#   | - check_moves()   - check if there are any legal moves possible; return a 
# dictionary with possible move {'queen': a7, 'rook': a6} for example; return 
# end of game signal if no moves are possible to def the king
#   - end_game()    - ends the game

class InvalidMove(Exception);
    pass

class Engine():
    start():
        pass

class Piece():
    colors = ['white', 'black']
    self.file = 0  # between a and h
    self.rank = 0  # between 1 and 8
    COLOR = enumerate(colors)  # COLOR[0] = white; COLOR[1] = black
    
    def check_values(self, file, rank):
        if file <

    def __init__(self):
        print ('You need to select an actual piece.')

    def location(self):
        return (self.file, str(self.rank))  # return a tuple ('a', '1')

    def check_move(self):  # An empty function to be inherited
        pass 

    def move(self, target):  # Move the piece at the target square 
        if target in check_move():
            self.file = target[0]
            self.rank = target[1]
            return (self.file, str(self.rank))
        else:
            raise InvalidMove('This is not a legal move')

class Pawn(Piece):
    
    def __init__(self, file, rank):
        self.check_values(file, rank)

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
