# This file defines the chess board

class Board():

    __init__(self):
        self.coordinates = [
                [a,b,c,d,e,f,g,h],  # 1
                [a,b,c,d,e,f,g,h],  # 2
                [a,b,c,d,e,f,g,h],  # 3
                [a,b,c,d,e,f,g,h],  # 4
                [a,b,c,d,e,f,g,h],  # 5
                [a,b,c,d,e,f,g,h],  # 6
                [a,b,c,d,e,f,g,h],  # 7
                [a,b,c,d,e,f,g,h]   # 8
                    ]
class Piece():

    __init__(self):
        
        # Ranks in chess are the rows of the board and they are numbered from 1-8
        self.position_rank = 0

        # Files in chess are the columns on the board and they are named using letters from a-h
        self.position_file = 0


class Pawn(Piece):
    
    __init__(self, pos_rank, pos_file):
        self.position_rank = pos_rank
        self.position_file = pos_file
    
    check_moves():
        # I neeed a color to know what direction the pawn has to move
        # to do that I may need a different class or property

    move():
        check_moves()   # check what moves are available, then make a decisionm (move/take)
        pass

# Note: the board can be expressed as list of lists, where each subsequent list is a row
board_lol=[
         [a,b,c,d,e,f,g,h],
         [a,b,c,d,e,f,g,h],
         [a,b,c,d,e,f,g,h],
         [a,b,c,d,e,f,g,h],
         [a,b,c,d,e,f,g,h],
         [a,b,c,d,e,f,g,h],
         [a,b,c,d,e,f,g,h],
         [a,b,c,d,e,f,g,h]
         ]

# Note: It can also be expressed as a list of dictionaries for easier interpretation

board_lod = [
         {a8: 5, b8: 3, c8: 3, d8: 9, e8: 100, f8: 3, g8: 3, h8: 5},
         {a7: 1, b7: 1, c7: 1, d7: 1, e7: 1, f7: 1, g7: 1, h7: 1},
         {a6: 0, b6: 0, c6: 0, d6: 0, e6: 0, f6: 0, g6: 0, h6: 0},
         {a5: 0, b5: 0, c5: 0, d5: 0, e5: 0, f5: 0, g5: 0, h5: 0},
         {a4: 0, b4: 0, c4: 0, d4: 0, e4: 0, f4: 0, g4: 0, h4: 0},
         {a3: 0, b3: 0, c3: 0, d3: 0, e3: 0, f3: 0, g3: 0, h3: 0),
         (a2: 1, b2: 1, c2: 1. d2: 1, e2: 1, f2: 1, g2: 1, h2: 1},
         {a1: 5, b1: 3, c1: 3, d1: 100, e1: 9, f1: 3, g1: 3, h1: 5},
        ]
