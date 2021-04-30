# This file defines the chess board

class Board():

    def generate_board(self):
        board = []
        colour_counter = 1
        for rank in self.ranks:
            for __file in self.files:
                if colour_counter % 2 == 0:
                    board.append([__file, rank, 'white'])
                    colour_counter = colour_counter + 1
                else:
                    board.append([__file, rank, 'black'])
                    colour_counter = colour_counter + 1
        return board

    def __init__(self):
        self.ranks = [1, 2, 3, 4, 5, 6, 7, 8]
        self.files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.board = self.generate_board()
       
    def read_notation(self):
        # K - king
        # Q - queen
        # R - rook
        # B - Bishop
        # _ - pawn - pawns don't have an encopding. Moving a pawn is done through the target square
        pass

    # Can I implement moves of the pieces as decorators of a general move function???

class Piece(): 

    def __init__(self, pos_rank = 0, pos_file = 0, col = None): 
        # Ranks in chess are the rows of the board and they are numbered from 1-8
        self.position_rank = pos_rank

        # Files in chess are the columns on the board and they are named using letters from a-h
        self.position_file = pos_file

        # Colour of the piece
        self.colour = col
        
        # Sets the value for the current piece
        self.value = 0

    # Check what moves are available
    def check_for_moves(self):
        pass

# A question stands with how do I check for other pieces. I can with checking if a square is ocupied or not.
# But to that I need a way to accesss each square on the board and assign it a value that shows whether or not 
# it is ocupied. Now how do I do that?

#   -   What if we make it so the pieces accept a board object during initiation. This would allow for scalability
# by making it possible to have multiple boards at the same time.

class Pawn(Piece):
    
    def __init__(self, pos_rank = 0, pos_file = 0, col = "white"):
        super().__init__(pos_rank, pos_file, col)
    
    def get_position(self):
        pos_list = []
        pos_list.append(self.position_rank)
        pos_list.append(self.position_file)
        return pos_list

    def check_for_moves(self):
        if (self.colour=="white"):
            self.pos = self.get_position()  # Shows as a list [row,file]
            
            print(self.pos)
        else:
            pass

    def move():
        check_moves()   # check what moves are available, then make a decisionm (move/take)
        pass

class Knight(Piece):
    def __init__(self, pos_rank = 0, pos_file = 0, col = "white"):
        super().__init__(pos_rank, pos_file, col)
        
    def get_position(self):
        pos_list = []
        pos_list.append(self.position_rank)
        pos_list.append(self.position_file)
        return pos_list

class Bishop(Piece):
    
    def __init__(self, pos_rank = 0, pos_file = 0, col = "white"):
        super().__init__(pos_rank, pos_file, col)
    
    def get_position(self):
        pos_list = []
        pos_list.append(self.position_rank)
        pos_list.append(self.position_file)
        return pos_list

class Rook(Piece):
    
    def __init__(self, pos_rank = 0, pos_file = 0, col = "white"):
        super().__init__(pos_rank, pos_file, col)
    
    def get_position(self):
        pos_list = []
        pos_list.append(self.position_rank)
        pos_list.append(self.position_file)
        return pos_list

class Queen(Piece):
    
    def __init__(self, pos_rank = 0, pos_file = 0, col = "white"):
        super().__init__(pos_rank, pos_file, col)
    
    def get_position(self):
        pos_list = []
        pos_list.append(self.position_rank)
        pos_list.append(self.position_file)
        return pos_list

class King(Piece):
    
    def __init__(self, pos_rank = 0, pos_file = 0, col = "white"):
        super().__init__(pos_rank, pos_file, col)
    
    def get_position(self):
        pos_list = []
        pos_list.append(self.position_rank)
        pos_list.append(self.position_file)
        return pos_list

# Note: the board can be expressed as list of lists, where each subsequent list is a row 

# board_lol=[
#          [a,b,c,d,e,f,g,h],
#          [a,b,c,d,e,f,g,h],
#          [a,b,c,d,e,f,g,h],
#          [a,b,c,d,e,f,g,h],
#          [a,b,c,d,e,f,g,h],
#          [a,b,c,d,e,f,g,h],
#          [a,b,c,d,e,f,g,h],
#          [a,b,c,d,e,f,g,h]
#          ]

# Note: It can also be expressed as a list of dictionaries for easier interpretation
# TODO: remember to make all keys strings since python things of them as variables otherwise

# board_lod = [
#          {a8: 5, b8: 3, c8: 3, d8: 9, e8: 100, f8: 3, g8: 3, h8: 5},
#          {a7: 1, b7: 1, c7: 1, d7: 1, e7: 1, f7: 1, g7: 1, h7: 1},
#          {a6: 0, b6: 0, c6: 0, d6: 0, e6: 0, f6: 0, g6: 0, h6: 0},
#          {a5: 0, b5: 0, c5: 0, d5: 0, e5: 0, f5: 0, g5: 0, h5: 0},
#          {a4: 0, b4: 0, c4: 0, d4: 0, e4: 0, f4: 0, g4: 0, h4: 0},
#          {a3: 0, b3: 0, c3: 0, d3: 0, e3: 0, f3: 0, g3: 0, h3: 0},
#          {a2: 1, b2: 1, c2: 1, d2: 1, e2: 1, f2: 1, g2: 1, h2: 1},
#          {a1: 5, b1: 3, c1: 3, d1: 100, e1: 9, f1: 3, g1: 3, h1: 5},
#         ]

pawn = Pawn(pos_rank=2, pos_file='a', col='white')

pawn.check_for_moves()

board = Board()
print(type(board))
