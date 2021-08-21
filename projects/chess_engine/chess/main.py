from custom_errors.errors import *
from pieces.pieces import *
from pprint import pprint

class Board():
    self.start_pos = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    self.ranks = [_ for _ in range(1, 9)] 
    self.board = self.gen_board()

    def __init__(self, position = '', new_game = True):
        self.files = [chr(i + 96) for i in range(1, 9)]
        
        if new_game: piece_coordinates = self.read(self.start_pos)
        else: piece_coordinates = self.read(position)        
        pieces_to_board(piece_coordinates)
    
    def pieces_to_board(self, obj_dict):
        for key in obj_dict: # key = 'a1'
            self.board[key] = obj_dict[key]
        
    # Generate a board
    def gen_board(self):
        '''
        Generate an empty dictionary that uses coordinates for keys.
        board = {
            'a1':None, 'a2':None, 'a3':None, ..., 'a8':None,
            'b1':None, 'b2':None, 'b3':None, ..., 'b8':None,
            ...
            'h1':None, 'h2':None, 'h3':None, ..., 'h8':None
        }
        '''
        board = {}
        for _file in self.files:
            for rank in self.ranks:
                key = _file + str(rank)
                board[key] = None
        return board

    def read(self, string):
        '''
        Reads the FEN transcript of the starting position
        '''
        # TBD what will be done with these variables
        # next_move = self.next_move(fen[1])
        # next_move = fen[1] # 'white' or 'black'
        # castling = fen[2]  # which side is available for castling - 'king'/'queen'
        # en_passant = fen[3]# what are the coordinates of a valid en passant
        # half_moves = fen[4]# how many half moves have been made since last capture or pawn advancement
        # moves = fen[5]     # how many hole moves have been made
        fen = string.split()
        board_state = fen[0].split('/')
        piece_coordinates = self.state_to_obj(board_state, piece_coordinates)
        return piece_coordinates

    # Convert Fen to a dict of objects
    def state_to_obj(fen, obj_dict):
        # Fen comes in the following form: [rnbqkbnr,pppppppp,8,8,8,8,PPPPPPPP,RNBQKBNR]
        actual_rank = 8
        for rank in range(0, len(fen)): # values for rank - 1 to 8; actual based on notaion - 8 to 1
            parse_string_notation(fen[rank], actual_rank)
            actual_rank -= 1
        return obj_dict

    def parse_string_notation(string, rank):
        on_rank = []
        tmp_file = 'a'
        for letter in string:
            if letter.isdecimal(): 
                for i in range(1, int(letter)):
                    on_rank.append(None)
                    tmp_file = chr(ord(tmp_file) + 1)
            elif letter.isalpha():
                on_rank.append(transcribe(letter, tmp_file, rank))
                tmp_file = chr(ord(tmp_file) + 1)
        return on_rank

    def transcribe(key, file, rank):
        tmp_file = file
        tmp_rank = rank
        transcript = {
            'p': Pawn(tmp_file, tmp_rank, 'black'),
            'P': Pawn(tmp_file, tmp_rank, 'white'),
            'r': Rook(tmp_file, tmp_rank, 'black'),
            'R': Rook(tmp_file, tmp_rank, 'white'),
            'n': Knight(tmp_file, tmp_rank, 'black'),
            'N': Knight(tmp_file, tmp_rank, 'white'),
            'b': Bishop(tmp_file, tmp_rank, 'black'),
            'B': Bishop(tmp_file, tmp_rank, 'white'),
            'q': Queen(tmp_file, tmp_rank, 'black'),
            'Q': Queen(tmp_file, tmp_rank, 'white'),
            'k': King(tmp_file, tmp_rank, 'black'),
            'K': King(tmp_file, tmp_rank, 'white'),
        }
        return transcript[key]

# ======================= Extras ======================== #

    def puzzle(self, position = ''):
        '''
        Create a board instance with specific piece positioning 
        for puzzles
        '''
        if position == '': 
            raise UndefinedGame("You haven't specified a starting position")
        else:
            self.__init__(position = position, new_game = False)

class Engine():

    def start():
        pass

    def save():
        pass

    def end():
        pass

if __name__ == '__main__':

    puzzle = 'a2w a3b Bb3w Kd3w e3w h3w Rb4b g4w Ke5b Ra6w Bb6b e6b g6b h6b' # Check the daily puzzle on chess.com

    b = Board(start)
    # pprint (b.board) # It actually worked xD heh kek :D
