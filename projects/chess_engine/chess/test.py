#self.new_game_setup = {
#            # Black pieces
#            'a8':Rook  ('a', 8, 'black'),
#            'b8':Knight('b', 8, 'black'),
#            'c8':Bishop('c', 8, 'black'),
#            'd8':Queen ('d', 8, 'black'),
#            'e8':King  ('e', 8, 'black'),
#            'f8':Bishop('f', 8, 'black'),
#            'g8':Knight('g', 8, 'black'),
#            'h8':Rook  ('h', 8, 'black'),
#            # Black pawns
#            'a7':Pawn('a', 7, 'black'),
#            'b7':Pawn('b', 7, 'black'),
#            'c7':Pawn('c', 7, 'black'),
#            'd7':Pawn('d', 7, 'black'),
#            'e7':Pawn('e', 7, 'black'),
#            'f7':Pawn('f', 7, 'black'),
#            'g7':Pawn('g', 7, 'black'),
#            'h7':Pawn('h', 7, 'black'),
#            # White pieces
#            'a1':Rook  ('a', 1, 'black'),
#            'b1':Knight('b', 1, 'black'),
#            'c1':Bishop('c', 1, 'black'),
#            'd1':Queen ('d', 1, 'black'),
#            'e1':King  ('e', 1, 'black'),
#            'f1':Bishop('f', 1, 'black'),
#            'g1':Knight('g', 1, 'black'),
#            'h1':Rook  ('h', 1, 'black'),
#            # Black pawns
#            'a2':Pawn('a', 2, 'black'),
#            'b2':Pawn('b', 2, 'black'),
#            'c2':Pawn('c', 2, 'black'),
#            'd2':Pawn('d', 2, 'black'),
#            'e2':Pawn('e', 2, 'black'),
#            'f2':Pawn('f', 2, 'black'),
#            'g2':Pawn('g', 2, 'black'),
#            'h2':Pawn('h', 2, 'black'), 
#}

#def def_piece(letter):
#    if str(letter) == 'r':
#        return '__Rook__'
#    else: return None
#
#board = {}
#files = [chr(i + 96) for i in range(1, 9)]
#ranks = [_ for _ in range(1, 9)]
#for f in files:
#    for r in ranks:
#        key = f + str(r)
#        board[key] = None
#
## example = 'rnbqkbnr/pppppppp/88888888/88888888/88888888/88888888/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
## string = example.split() 
## print (string[0])
## setup = string[0].split('/') # [rnbqkbnr pppppppp 8 8 8 8 PPPPPPPP RNBQKBNR]
## print (setup)
## i = 0
## for rank in range (len(setup), 0, -1): # from 8 to 1
##     j = 0
##     for f in files:
##         key = f + str(rank)
##         print (key)
##         board[key] = def_piece(setup[j])
##         j += 1
##     i += 1
## print (board) 
#
#def state_to_obj(fen, obj_dict):
#    # Fen comes in the following form: [rnbqkbnr,pppppppp,8,8,8,8,PPPPPPPP,RNBQKBNR]
#    actual_rank = 8
#    for rank in range(0, len(fen)): # values for rank - 1 to 8; actual based on notaion - 8 to 1
#        parse_string_notation(fen[rank], actual_rank)
#        actual_rank -= 1
#    return obj_dict
#
## A really dumb way to make thing dynamic is to use globals. Essentially I don't know why 
## it's dumb, but smarter people say it is so I guess I will go with I am a noob :D
#def parse_string_notation(string, rank):
#    on_rank = []
#    tmp_file = 'a'
#    for letter in string:
#        if letter.isdecimal(): 
#            for i in range(1, int(letter)):
#                on_rank.append(None)
#                tmp_file = chr(ord(tmp_file) + 1)
#        elif letter.isalpha():
#            # global tmp_file = 
#            # global tmp_rank = 
#            on_rank.append(transcribe(letter, tmp_file, rank))
#            tmp_file = chr(ord(tmp_file) + 1)
#    print (on_rank)
#    return on_rank
#
#def transcribe(key, file, rank):
#    tmp_file = file
#    tmp_rank = rank
#    transcript = {
#        'p': '__Pawn__.{}{}'.format(tmp_file, tmp_rank),
#        'P': '__Pawn__.{}{}'.format(tmp_file, tmp_rank),
#        'r': '__Rook__.{}{}'.format(tmp_file, tmp_rank),
#        'R': '__Rook__.{}{}'.format(tmp_file, tmp_rank),
#        'n': '__Knight__.{}{}'.format(tmp_file, tmp_rank),
#        'N': '__Knight__.{}{}'.format(tmp_file, tmp_rank),
#        'b': '__Bishop__.{}{}'.format(tmp_file, tmp_rank),
#        'B': '__Bishop__.{}{}'.format(tmp_file, tmp_rank),
#        'q': '__Queen__.{}{}'.format(tmp_file, tmp_rank),
#        'Q': '__Queen__.{}{}'.format(tmp_file, tmp_rank),
#        'k': '__King__.{}{}'.format(tmp_file, tmp_rank),
#        'K': '__King__.{}{}'.format(tmp_file, tmp_rank),
#    }
#    return transcript[key]
#    
#
#dic = {}
#example = 'rnbqkbnr/ppp1pppp/3p4/8/4P3/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
#string = example.split() 
#setup = string[0].split('/') # [rnbqkbnr pppppppp 8 8 8 8 PPPPPPPP RNBQKBNR]
#
#print (state_to_obj(setup, dic))


