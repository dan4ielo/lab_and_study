# from chess.custom_errors.errors import *

#========== UNIVERSAL characteristic ==========#
valid_files = [ord('a'), ord('b'), ord('c'), 
               ord('d'), ord('e'), ord('f'),
               ord('g'), ord('h')]
valid_ranks = [1, 2, 3, 4, 5, 6, 7, 8]

#========== PAWN movement ==========#
def pawn_rank_movement(loc, color):
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

def pawn_file_movement(loc):
    moves = []
    file = loc[0]
    rank = loc[1]
    # if (check for takes):
    #     moves.append(chr(ord(file) +- 1) , rank)
    # NOTE This method needs to be called from the board
    return moves

def pawn_movement(loc, color):
    moves = []
    for move in pawn_rank_movement(loc, color):
        moves.append(move)
    for move in pawn_file_movement(loc):
        moves.append(move)
    return moves

#========== KNIGHT movement ==========#
def front_back_moves(loc):
    moves = []
    file = loc[0]
    rank = loc[1]
    if rank + 2 in valid_ranks: rank_up = rank + 2
    else: rank_up = None
    if rank - 2 in valid_ranks: rank_down = rank - 2
    else: rank_down = None
    if ord(file) + 1 in valid_files: file_right = chr(ord(file) + 1)
    else: file_right = None
    if ord(file) - 1 in valid_files: file_left = chr(ord(file) - 1)
    else: file_left = None

    moves.append((file_left, rank_up))
    moves.append((file_right, rank_up))
    moves.append((file_left, rank_down))
    moves.append((file_right, rank_down))
    moves = [move for move in moves if move[0] != None and move[1] != None]
    return moves

def left_right_moves(loc):
    moves = []
    file = loc[0]
    rank = loc[1]
    # The None values help prevent Unbound Local Errors
    if rank + 1 in valid_ranks: rank_up = rank + 1
    else: rank_up = None
    if rank - 1 in valid_ranks: rank_down = rank - 1
    else: rank_down = None
    if ord(file) + 2 in valid_files: file_right = chr(ord(file) + 2)
    else: file_right = None
    if ord(file) - 2 in valid_files: file_left = chr(ord(file) - 2)
    else: file_left = None

    moves.append((file_left, rank_up))
    moves.append((file_right, rank_up))
    moves.append((file_left, rank_down))
    moves.append((file_right, rank_down))
    moves = [move for move in moves if move[0] != None and move[1] != None]
    return moves

def knight_movement(loc):
    moves = []
    for move in front_back_moves(loc):
        moves.append(move)
    for move in left_right_moves(loc):
        moves.append(move)
    return moves

#========== BISHOP movement ==========#
def left_down(loc):
    moves = []
    file = loc[0]
    rank = loc[1]
    while ord(file) in valid_files and rank in valid_ranks:
        move = (file, rank)
        file = chr(ord(file) - 1)
        rank -= 1
        moves.append(move)
    moves = [move for move in moves if 0 not in move]
    return moves

def left_up(loc):
    moves = []
    file = loc[0]
    rank = loc[1]
    while ord(file) in valid_files and rank in valid_ranks:
        move = (file, rank)
        file = chr(ord(file) - 1)
        rank += 1
        moves.append(move)
    moves = [move for move in moves if 0 not in move]
    return moves

def right_up(loc):
    moves = []
    file = loc[0]
    rank = loc[1]
    while ord(file) in valid_files and rank in valid_ranks:
        move = (file, rank)
        file = chr(ord(file) + 1)
        rank += 1
        moves.append(move)
    moves = [move for move in moves if 0 not in move]
    return moves

def right_down(loc):
    moves = []
    file = loc[0]
    rank = loc[1]
    while ord(file) in valid_files and rank in valid_ranks:
        move = (file, rank)
        file = chr(ord(file) + 1)
        rank -= 1
        moves.append(move)
    moves = [move for move in moves if 0 not in move]
    return moves

def bishop_movement(loc):
    moves = []
    for move in left_up(loc):
        moves.append(move)
    for move in left_down(loc):
        moves.append(move)
    for move in right_up(loc):
        moves.append(move)
    for move in right_down(loc):
        moves.append(move)
    moves = list(set(moves))
    moves.remove(loc)
    return moves


#========== ROOK movement ==========#
def left(loc):
    moves = []
    file = loc[0]
    rank = loc[1]
    while ord(file) in valid_files:
        move = (file, rank)
        file = chr(ord(file) - 1)
        moves.append(move)
    return moves

def right(loc):
    moves = []
    file = loc[0]
    rank = loc[1]
    while ord(file) in valid_files:
        move = (file, rank)
        file = chr(ord(file) + 1)
        moves.append(move)
    return moves

def up(loc):
    moves = []
    file = loc[0]
    rank = loc[1]
    while rank in valid_ranks:
        move = (file, rank)
        rank += 1
        moves.append(move)
    return moves

def down(loc):
    moves = []
    file = loc[0]
    rank = loc[1]
    while rank in valid_ranks:
        move = (file, rank)
        rank -= 1
        moves.append(move)
    return moves

def rook_movement(loc):
    moves = []
    for move in left(loc):
        moves.append(move)
    for move in down(loc):
        moves.append(move)
    for move in up(loc):
        moves.append(move)
    for move in right(loc):
        moves.append(move)
    moves = list(set(moves))
    moves.remove(loc)
    return moves

#========== KING movement ==========#


def king_movement(loc):
    moves = []
    file = loc[0]
    rank = loc[1]
    if ord(file) + 1 in valid_files and rank + 1 in valid_ranks:
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

if __name__ == "__main__":
    print (rook_movement(('a', 1)))
    print (left(('a', 1)))
    print (right(('a', 1)))
    print (up(('a', 1)))
    print (down(('a', 1)))
